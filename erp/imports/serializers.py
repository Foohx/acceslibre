import re

from django.contrib.gis.geos import Point
from django.forms.models import model_to_dict
from rest_framework import serializers

from erp.imports.utils import get_address_query_to_geocode
from erp.models import Accessibilite, Activite, Commune, Erp
from erp.provider import geocoder, sirene


class DuplicatedExceptionErp(serializers.ValidationError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, code="duplicate")


class AccessibilityImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessibilite
        fields = "__all__"


class ErpImportSerializer(serializers.ModelSerializer):
    activite = serializers.SlugRelatedField(queryset=Activite.objects.all(), slug_field="nom")
    commune = serializers.CharField(required=True)
    accessibilite = AccessibilityImportSerializer(many=False, required=True)
    latitude = serializers.FloatField(min_value=-90, max_value=90, required=False, allow_null=True, default=None)
    longitude = serializers.FloatField(min_value=-180, max_value=180, required=False, allow_null=True, default=None)
    _geom: Point = None

    class Meta:
        model = Erp
        fields = (
            "nom",
            "code_postal",
            "commune",
            "numero",
            "voie",
            "lieu_dit",
            "code_insee",
            "siret",
            "contact_url",
            "activite",
            "import_email",
            "site_internet",
            "accessibilite",
            "latitude",
            "longitude",
            "source",
        )

    def validate_siret(self, obj):
        if not obj:
            return

        cleaned = sirene.validate_siret(obj)
        if not cleaned:
            raise serializers.ValidationError("Le siret doit être valide.")

        return cleaned

    def validate_code_postal(self, obj):
        # source: https://rgxdb.com/
        if not re.match(r"^(?:0[1-9]|[1-8]\d|9[0-8])\d{3}$", obj):
            raise serializers.ValidationError("Le code postal n'est pas valide.")

        return obj

    def validate_accessibilite(self, obj):
        if not obj:
            raise serializers.ValidationError("Au moins un champ d'accessibilité requis.")

        return obj

    def validate(self, obj):
        if self.instance:
            # if we are updating an ERP, only accessibility is editable
            accessibilite = Accessibilite(**obj["accessibilite"])
            accessibilite.full_clean()
            return model_to_dict(self.instance) | {"accessibilite": model_to_dict(accessibilite)}

        if not obj.get("voie") and not obj.get("lieu_dit"):
            raise serializers.ValidationError("Veuillez entrer une voie OU un lieu-dit")

        for i in range(3):
            try:
                address = get_address_query_to_geocode(obj)
                locdata = geocoder.geocode(address, postcode=obj["code_postal"])
                if not locdata:
                    raise RuntimeError
                self._geom = locdata["geom"]
                obj["voie"] = locdata["voie"]
                obj["lieu_dit"] = locdata["lieu_dit"]
                obj["code_postal"] = locdata["code_postal"]
                obj["commune"] = locdata["commune"]
                obj["code_insee"] = locdata["code_insee"]
                obj.pop("latitude", None)
                obj.pop("longitude", None)
                break
            except (RuntimeError, KeyError):
                if i < 2:
                    continue

                if obj.get("latitude") is not None and obj.get("longitude") is not None:
                    self._geom = Point((obj["latitude"], obj["longitude"]))
                    obj.pop("latitude")
                    obj.pop("longitude")
                    break

                raise serializers.ValidationError(f"Adresse non localisable: {address}")

        obj["commune_ext"] = Commune.objects.filter(
            nom__iexact=obj["commune"], code_postaux__contains=[obj["code_postal"]]
        ).first()

        existing = Erp.objects.find_duplicate(
            numero=obj.get("numero"),
            voie=obj.get("voie"),
            lieu_dit=obj.get("lieu_dit"),
            commune=obj["commune"],
            activite=obj["activite"],
        ).first()

        if existing:
            raise DuplicatedExceptionErp(f"Potentiel doublon avec l'ERP : {existing}")

        erp_data = obj.copy()
        erp_data.pop("accessibilite")
        Erp(**erp_data).full_clean(exclude=("source_id", "asp_id", "user", "metadata", "search_vector"))
        Accessibilite(**obj["accessibilite"]).full_clean()
        return obj

    def update(self, instance, validated_data, partial=True):
        accessibilite = instance.accessibilite
        for attr in ("id", "erp"):
            validated_data["accessibilite"].pop(attr, False)

        for attr in validated_data["accessibilite"]:
            setattr(accessibilite, attr, validated_data["accessibilite"][attr])

        accessibilite.save()
        return instance

    def create(self, validated_data):
        accessibilite_data = validated_data.pop("accessibilite")
        erp = Erp.objects.create(**validated_data, geom=self._geom)
        Accessibilite.objects.create(erp=erp, **accessibilite_data)

        return erp
