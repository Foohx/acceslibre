# Generated by Django 3.2.13 on 2022-09-30 08:09

import django.contrib.postgres.fields
from django.db import migrations, models

import erp.models


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0140_auto_20220901_1426"),
    ]

    operations = [
        migrations.AddField(
            model_name="erp",
            name="itm_id",
            field=models.CharField(
                help_text="Identifiant de l'ERP dans la base Service Public",
                max_length=255,
                null=True,
                verbose_name="ITM ID",
            ),
        ),
        migrations.AlterField(
            model_name="accessibilite",
            name="accueil_equipements_malentendants",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("bim", "boucle à induction magnétique fixe"),
                        ("bmp", "boucle à induction magnétique portative"),
                        ("lsf", "langue des signes française (LSF)"),
                        ("lpc", "langue française parlée complétée (LFPC)"),
                        ("sts", "sous-titrage ou transcription simultanée"),
                        ("autres", "autres"),
                    ],
                    max_length=255,
                ),
                blank=True,
                default=list,
                null=True,
                size=None,
                verbose_name="Équipement(s) sourd/malentendant",
            ),
        ),
        migrations.AlterField(
            model_name="activite",
            name="position",
            field=models.PositiveSmallIntegerField(
                default=erp.models.get_last_position,
                verbose_name="Position dans la liste",
            ),
        ),
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
                    ("centres-vaccination", "Centres de vaccination"),
                ],
                default="public",
                help_text="Nom de la source de données dont est issu cet ERP",
                max_length=100,
                null=True,
                verbose_name="Source",
            ),
        ),
    ]
