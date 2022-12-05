# Generated by Django 3.2.16 on 2022-11-23 14:46

import uuid

import autoslug.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

from stats.models import GlobalStats


def create_global_stats(*args, **kwargs):
    GlobalStats.refresh_stats()


def dedoublonnage_referer(apps, schema_editor):
    Referer = apps.get_model("stats", "referer")
    referers = Referer.objects.values("domain").distinct()

    for e in referers:
        list_referer = (
            Referer.objects.filter(domain=e["domain"])
            .order_by("date_notification_to_mattermost")[1:]
            .values_list("pk", flat=True)
        )
        Referer.objects.filter(pk__in=list_referer).delete()


def dedoublonnage_implementation(apps, schema_editor):
    Implementation = apps.get_model("stats", "implementation")
    implementations = Implementation.objects.values("urlpath").distinct()

    for e in implementations:
        list_implementation = (
            Implementation.objects.filter(urlpath=e["urlpath"]).order_by("created_at")[1:].values_list("pk", flat=True)
        )
        Implementation.objects.filter(pk__in=list_implementation).delete()


class Migration(migrations.Migration):

    replaces = [
        ("stats", "0001_initial"),
        ("stats", "0002_alter_challenge_start_date"),
        ("stats", "0003_auto_20220502_1520"),
        ("stats", "0004_implementation_referer"),
        ("stats", "0005_auto_20220509_0913"),
        ("stats", "0006_manual_implementation"),
        ("stats", "0007_auto_20220512_1331"),
        ("stats", "0008_auto_20220518_2242"),
        ("stats", "0009_auto_20220616_0815"),
        ("stats", "0010_globalstats"),
        ("stats", "0011_auto_20220622_1127"),
        ("stats", "0012_auto_20220630_1040"),
        ("stats", "0013_auto_20221017_1247"),
        ("stats", "0014_auto_20221017_1257"),
        ("stats", "0015_auto_20221017_1549"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Challenge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("nom", models.CharField(help_text="Nom du challenge", max_length=255)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        default="",
                        editable=False,
                        help_text="Identifiant d'URL (slug)",
                        max_length=255,
                        populate_from="nom",
                        unique=True,
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(verbose_name="Date de début du challenge"),
                ),
                (
                    "end_date",
                    models.DateTimeField(verbose_name="Date de fin du challenge (inclus)"),
                ),
                ("nb_erp_total_added", models.BigIntegerField(default=0)),
                ("classement", models.JSONField(default=dict)),
                ("active", models.BooleanField(default=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Créateur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Challenge",
                "verbose_name_plural": "Challenges",
                "ordering": ("nom",),
            },
        ),
        migrations.CreateModel(
            name="Referer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("domain", models.URLField(help_text="Domaine du site réutilisateur")),
                (
                    "date_notification_to_mattermost",
                    models.DateTimeField(null=True, verbose_name="Date de notification sur Mattermost ?"),
                ),
            ],
            options={
                "verbose_name": "Site réutilisateur",
                "verbose_name_plural": "Sites réutilisateur",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Implementation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("urlpath", models.URLField(help_text="Url complète")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date de détection de tracking"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Date de dernier contact"),
                ),
                (
                    "referer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="implementations",
                        to="stats.referer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Implémentation du Widget",
                "verbose_name_plural": "Implémentations du Widget",
                "ordering": ("-updated_at", "urlpath"),
            },
        ),
        migrations.RunPython(
            code=dedoublonnage_referer,
        ),
        migrations.RunPython(
            code=dedoublonnage_implementation,
        ),
        migrations.AlterField(
            model_name="implementation",
            name="urlpath",
            field=models.URLField(help_text="Url complète", unique=True),
        ),
        migrations.AlterField(
            model_name="referer",
            name="domain",
            field=models.URLField(help_text="Domaine du site réutilisateur", unique=True),
        ),
        migrations.AddIndex(
            model_name="implementation",
            index=models.Index(fields=["referer"], name="referer_idx"),
        ),
        migrations.AddIndex(
            model_name="implementation",
            index=models.Index(fields=["urlpath"], name="urlpath_idx"),
        ),
        migrations.AddIndex(
            model_name="referer",
            index=models.Index(fields=["domain"], name="domain_idx"),
        ),
        migrations.CreateModel(
            name="GlobalStats",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "_singleton",
                    models.BooleanField(default=True, editable=False, unique=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("erp_counts_histogram", models.JSONField(default=dict)),
                ("stats_territoires_sort_count", models.JSONField(default=dict)),
                ("stats_territoires_sort_default", models.JSONField(default=dict)),
                ("top_contributors", models.JSONField(default=dict)),
            ],
            options={
                "verbose_name": "Statistiques",
                "verbose_name_plural": "Statistiques",
            },
        ),
        migrations.RunPython(
            code=create_global_stats,
        ),
        migrations.AddField(
            model_name="challenge",
            name="accroche",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="objectif",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="ChallengePlayer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "inscription_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription"),
                ),
                (
                    "challenge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="stats.challenge",
                        verbose_name="Challenge",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Joueur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Challenge Player",
                "verbose_name_plural": "Challenges Players",
                "ordering": ("inscription_date",),
            },
        ),
        migrations.AddField(
            model_name="challenge",
            name="players",
            field=models.ManyToManyField(
                related_name="challenge_players",
                through="stats.ChallengePlayer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="challengeplayer",
            name="challenge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="inscriptions",
                to="stats.challenge",
                verbose_name="Challenge",
            ),
        ),
        migrations.AlterField(
            model_name="challengeplayer",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="inscriptions",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Joueur",
            ),
        ),
    ]
