import logging

import requests
from django.contrib.gis.geos import Point

from core.lib import geo

logger = logging.getLogger(__name__)

GEOCODER_URL = "https://api-adresse.data.gouv.fr/search/"


def autocomplete(q, limit=1):
    params = {
        "autocomplete": 1,
        "q": q,
        "limit": limit,
    }
    try:
        results = query(params, timeout=0.75)  # avoid blocking for too long
        (lon, lat) = results.get("features")[0]["geometry"]["coordinates"]
        return geo.parse_location((lat, lon))
    except (KeyError, IndexError, RuntimeError):
        return None


def geocode(adresse, postcode=None, citycode=None):
    try:
        data = query({"q": adresse, "postcode": postcode, "citycode": citycode, "limit": 1})
        feature = data["features"][0]
        # print(json.dumps(data, indent=2))
        properties = feature["properties"]
        type = properties["type"]
        # result type handling
        voie = None
        lieu_dit = None
        if type == "street":
            voie = properties.get("name")
        elif type == "housenumber":
            voie = properties.get("street")
        elif type == "locality":
            lieu_dit = properties.get("name")
        # score
        if properties["score"] < 0.5:
            return None
        # coordinates
        geometry = feature["geometry"]
        return {
            "geom": Point(geometry["coordinates"], srid=4326),
            "numero": properties.get("housenumber"),
            "voie": voie,
            "lieu_dit": lieu_dit,
            "code_postal": properties.get("postcode"),
            "commune": properties.get("city"),
            "code_insee": properties.get("citycode"),
        }
    except (KeyError, IndexError, TypeError) as err:
        raise RuntimeError(f"Erreur lors du géocodage de l'adresse {adresse}") from err


def query(params, timeout=8):
    try:
        res = requests.get(GEOCODER_URL, params, timeout=timeout)
        logger.info(f"Geocoder call: {res.url}")
        if res.status_code != 200:
            raise RuntimeError(f"Erreur HTTP {res.status_code} lors de la géolocalisation de l'adresse.")
        return res.json()
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        raise RuntimeError("Serveur de géocodage indisponible.")


def parse_coords(coords):
    "Returns a (lat, lon) tuple or None from a string"
    if coords is None:
        return None
    try:
        rlat, rlon = coords.split(",")
        return (float(rlat), float(rlon))
    except (IndexError, ValueError, TypeError):
        return None


def geocode_commune(code_insee):
    res = requests.get(
        "https://geo.api.gouv.fr/communes",
        {
            "fields": "code,nom,departement,centre,surface,population,codesPostaux",
            "limit": "1",
            "code": code_insee,
        },
    )
    json = res.json()
    return json[0] if len(json) > 0 else None
