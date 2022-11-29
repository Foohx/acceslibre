import re

from django.contrib.gis.geos import Point
from rest_framework import serializers

from erp.models import Accessibilite, Activite, Commune, Erp
from erp.provider import geocoder, sirene


class AccessibilityImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessibilite
        fields = "__all__"


class ErpImportSerializer(serializers.ModelSerializer):
    activite = serializers.SlugRelatedField(queryset=Activite.objects.all(), slug_field="nom")
    commune = serializers.SlugRelatedField(queryset=Commune.objects.all(), slug_field="nom")
    accessibilite = AccessibilityImportSerializer(many=False, required=True)
    latitude = serializers.FloatField(min_value=-90, max_value=90, required=False)
    longitude = serializers.FloatField(min_value=-180, max_value=180, required=False)
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
            "site_internet",
            "accessibilite",
            "latitude",
            "longitude",
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
        if not obj.get("voie") and not obj.get("lieu_dit"):
            raise serializers.ValidationError("Veuillez entrer une voie OU un lieu-dit")

        address = " ".join(
            [
                obj.get("numero") or "",
                obj.get("voie") or "",
            ]
        )
        address = ", ".join(
            [
                address,
                obj.get("lieu_dit") or "",
                obj["commune"].nom,
            ]
        )

        for i in range(3):
            try:
                locdata = geocoder.geocode(address, citycode=obj["commune"].code_insee)
                self._geom = locdata["geom"]
                break
            except (RuntimeError, KeyError):
                if i < 2:
                    continue

                if "latitude" in obj and "longitude" in obj:
                    self._geom = Point((obj["latitude"], obj["longitude"]))
                    obj.pop("latitude")
                    obj.pop("longitude")
                    break

                raise serializers.ValidationError(f"Adresse non localisable: {address}")

        return obj

    def create(self, validated_data):
        accessibilite_data = validated_data.pop("accessibilite")
        erp = Erp.objects.create(**validated_data, geom=self._geom)
        Accessibilite.objects.create(erp=erp, **accessibilite_data)

        return erp
