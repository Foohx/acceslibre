from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db import models
from django.db.models.aggregates import Count


class ActiviteManager(models.Manager):
    def with_erp_counts(self, commune=None, order_by=None):
        qs = self
        if commune is not None:
            qs = qs.filter(erp__commune__iexact=commune)
        qs = qs.annotate(count=Count("erp__activite")).filter(count__gt=0)
        if order_by is not None:
            qs = qs.order_by(order_by)
        else:
            qs = qs.order_by("-count")
        return qs


class ErpManager(models.Manager):
    def nearest(self, lon, lat):
        location = Point(lon, lat, srid=4326)
        return self.annotate(distance=Distance("geom", location)).order_by(
            "distance"
        )
