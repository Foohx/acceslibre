# Generated by Django 3.0.5 on 2020-04-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0066_auto_20200408_1015"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessibilite",
            name="transport_station_presence",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "Oui"), (False, "Non"), (None, "Inconnu")],
                help_text="Présence d'une station de transport en commun à proximité (500 m)",
                null=True,
                verbose_name="Stationnement dans l'ERP",
            ),
        ),
        migrations.AddField(
            model_name="erp",
            name="contact_email",
            field=models.CharField(
                blank=True,
                help_text="Adresse email permettant de contacter l'ERP",
                max_length=20,
                null=True,
                verbose_name="Courriel",
            ),
        ),
    ]
