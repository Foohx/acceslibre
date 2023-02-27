# Generated by Django 3.2.18 on 2023-02-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0151_accessibilite_completion_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="erp",
            name="geoloc_provider",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Indique le fournisseur utilisé pour la géolocalisation de l'adresse de l'ERP.",
                max_length=50,
                null=True,
                verbose_name="Fournisseur utilisé pour la géolocalisation",
            ),
        ),
    ]
