import uuid
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models

from stats.queries import get_count_challenge


class Challenge(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Créateur", on_delete=models.PROTECT
    )
    nom = models.CharField(max_length=255, help_text="Nom du challenge")
    slug = AutoSlugField(
        default="",
        unique=True,
        populate_from="nom",
        help_text="Identifiant d'URL (slug)",
        max_length=255,
    )
    start_date = models.DateTimeField(verbose_name="Date de début du challenge")
    end_date = models.DateTimeField(verbose_name="Date de fin du challenge (inclus)")
    nb_erp_total_added = models.BigIntegerField(default=0)
    classement = models.JSONField(default=dict)

    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("nom",)
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    def __str__(self):
        return self.nom

    def refresh_stats(self):
        classement, self.nb_erp_total_added = get_count_challenge(
            self.start_date, self.end_date
        )
        self.classement = [
            {"username": user.username, "erp_count_published": user.erp_count_published}
            for user in classement
        ]
        self.save()
