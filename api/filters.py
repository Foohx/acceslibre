from django.contrib.gis.geos import Point
from rest_framework.filters import BaseFilterBackend
from rest_framework_gis.filters import InBBoxFilter

from erp.provider import geocoder
from erp.provider.search import filter_erps_by_equipments


class ZoneFilter(InBBoxFilter):
    bbox_param = "zone"

    def get_schema_operation_parameters(self, view):
        return [
            {
                "name": self.bbox_param,
                "required": False,
                "in": "query",
                "description": "Coordonnées du cadre englobant la recherche au format `min_longitude,min_latitude,max_longitude,max_latitude` (par ex. ?zone=4.849022,44.885530,4.982661,44.963994)",
                "schema": {
                    "type": "array",
                    "items": {"type": "float"},
                    "minItems": 4,
                    "maxItems": 4,
                    "example": [-180, -90, 180, 90],
                },
                "style": "form",
                "explode": False,
            },
        ]


class ErpFilter(BaseFilterBackend):
    # FIXME: do NOT apply filters on details view
    def filter_queryset(self, request, queryset, view):
        use_distinct = False

        # Drafts
        with_drafts = request.query_params.get("with_drafts", False)
        if not with_drafts:
            queryset = queryset.published()

        # Commune (legacy)
        commune = request.query_params.get("commune", None)
        if commune is not None:
            queryset = queryset.filter(commune__unaccent__icontains=commune)

        # Code postal
        code_postal = request.query_params.get("code_postal", None)
        if code_postal is not None:
            queryset = queryset.filter(code_postal=code_postal)

        # Code INSEE
        code_insee = request.query_params.get("code_insee", None)
        if code_insee is not None:
            queryset = queryset.filter(commune_ext__code_insee=code_insee)

        # Activité
        activite = request.query_params.get("activite", None)
        if activite is not None:
            queryset = queryset.having_activite(activite)

        # SIRET
        siret = request.query_params.get("siret", None)
        if siret is not None:
            queryset = queryset.filter(siret=siret)

        # Search
        search_terms = request.query_params.get("q", None)
        if search_terms is not None:
            use_distinct = False
            queryset = queryset.search_what(search_terms)

        # Source Externe
        source = request.query_params.get("source", None)
        if source is not None:
            queryset = queryset.filter(source__iexact=source)

        # Id Externe
        source_id = request.query_params.get("source_id", None)
        if source_id is not None:
            queryset = queryset.filter(source_id__iexact=source_id)

        # ASP Id
        asp_id = request.query_params.get("asp_id", None)
        if asp_id is not None:
            queryset = queryset.filter(asp_id__iexact=asp_id)

        # ASP ID is not null
        asp_id_not_null = request.query_params.get("asp_id_not_null", None)
        if asp_id_not_null is not None:
            if asp_id_not_null == "true":
                queryset = queryset.exclude(asp_id__isnull=True).exclude(asp_id__exact="")
            else:
                queryset = queryset.filter(asp_id__isnull=True)

        # UUID
        uuid = request.query_params.get("uuid", None)
        if uuid is not None:
            queryset = queryset.filter(uuid=uuid)

        # Proximity
        around = geocoder.parse_coords(request.query_params.get("around"))
        if around is not None:
            lat, lon = around
            queryset = queryset.nearest(Point(lon, lat, srid=4326))
            use_distinct = False

        if use_distinct:
            queryset = queryset.distinct("id", "nom")
        return queryset


class EquipmentFilter(BaseFilterBackend):
    def get_schema_operation_parameters(self, view):
        return [
            {
                "name": "equipments",
                "in": "query",
                "required": False,
                "description": "Liste d'équipements que doivent posséder les établissements retournés (par ex. `?equipments=having_public_transportation&equipments=having_adapted_parking`)",
                "schema": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1,
                    "example": ["having_public_transportation", "having_adapted_parking"],
                },
            },
        ]

    def filter_queryset(self, request, queryset, *args, **kwargs):
        equipments = request.query_params.getlist("equipments")
        return filter_erps_by_equipments(queryset, equipments)
