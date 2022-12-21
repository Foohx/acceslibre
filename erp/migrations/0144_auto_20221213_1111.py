# Generated by Django 3.2.16 on 2022-12-13 10:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0143_erp_import_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessibilite",
            name="accueil_audiodescription",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("avec_équipement_permanent", "avec équipement permanent"),
                        ("avec_app", "avec application sur smartphone"),
                        ("avec_équipement_occasionnel", "avec équipement occasionnel"),
                        ("sans_équipement", "sans équipement"),
                    ],
                    max_length=255,
                ),
                blank=True,
                default=list,
                null=True,
                size=None,
                verbose_name="Équipement(s) audiodescription",
            ),
        ),
        migrations.AddField(
            model_name="accessibilite",
            name="accueil_audiodescription_presence",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "Oui"), (False, "Non"), (None, "Inconnu")],
                null=True,
                verbose_name="Audiodescription",
            ),
        ),
    ]
