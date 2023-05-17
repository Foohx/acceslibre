# Generated by Django 3.2.17 on 2023-02-09 16:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("erp", "0148_auto_20230102_1416"),
    ]

    operations = [
        migrations.AlterField(
            model_name="erp",
            name="source",
            field=models.CharField(
                choices=[
                    ("acceslibre", "Base de données Acceslibre"),
                    ("acceo", "Acceo"),
                    ("admin", "Back-office"),
                    ("api", "API"),
                    ("entreprise_api", "API Entreprise (publique)"),
                    ("cconforme", "cconforme"),
                    ("gendarmerie", "Gendarmerie"),
                    ("lorient", "Lorient"),
                    ("nestenn", "Nestenn"),
                    ("opendatasoft", "API OpenDataSoft"),
                    ("public", "Saisie manuelle publique"),
                    ("public_erp", "API des établissements publics"),
                    ("sap", "Sortir À Pair"),
                    ("service_public", "Service Public"),
                    ("sirene", "API Sirene INSEE"),
                    ("tourisme-handicap", "Tourisme & Handicap"),
                    ("typeform", "Questionnaires Typeform"),
                    ("typeform_musee", "Questionnaires Typeform Musée"),
                    ("centres-vaccination", "Centres de vaccination"),
                    ("dell", "Dell"),
                ],
                default="public",
                help_text="Nom de la source de données dont est issu cet ERP",
                max_length=100,
                null=True,
                verbose_name="Source",
            ),
        ),
        migrations.CreateModel(
            name="ActivitySuggestion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="Nom suggéré pour l'activité", max_length=255, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Date de création")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Dernière modification")),
                (
                    "erp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="erp.erp", verbose_name="Établissement"
                    ),
                ),
                (
                    "mapped_activity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="erp.activite",
                        verbose_name="Activité correspondante",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "verbose_name": "Suggestion d'activité",
                "verbose_name_plural": "Suggestions d'activités",
            },
        ),
    ]
