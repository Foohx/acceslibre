from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from reversion.models import Version

from .models import Accessibilite, Erp


def get_user_contributions(user):
    erp_type = ContentType.objects.get_for_model(Erp)
    accessibilite_type = ContentType.objects.get_for_model(Accessibilite)
    user_erps = [f["id"] for f in Erp.objects.filter(user=user).values("id")]
    user_accesses = [
        f["id"] for f in Accessibilite.objects.filter(erp__user=user).values("id")
    ]
    return (
        Version.objects.select_related("revision", "revision__user")
        .exclude(content_type=erp_type, object_id__in=user_erps)
        .exclude(content_type=accessibilite_type, object_id__in=user_accesses)
        .filter(
            Q(revision__user=user),
            Q(content_type=erp_type) | Q(content_type=accessibilite_type),
        )
        .prefetch_related("object")
    )


def get_user_contributions_recues(user):
    erp_type = ContentType.objects.get_for_model(Erp)
    accessibilite_type = ContentType.objects.get_for_model(Accessibilite)
    user_erps = [f["id"] for f in Erp.objects.filter(user=user).values("id")]
    user_accesses = [
        f["id"] for f in Accessibilite.objects.filter(erp__user=user).values("id")
    ]
    return (
        Version.objects.select_related("revision", "revision__user")
        .exclude(Q(revision__user=user) | Q(revision__user__isnull=True))
        .filter(
            Q(content_type=erp_type) | Q(content_type=accessibilite_type),
            Q(content_type=erp_type, object_id__in=user_erps)
            | Q(content_type=accessibilite_type, object_id__in=user_accesses),
        )
        .prefetch_related("object")
    )
