# Generated by Django 3.2.4 on 2021-06-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0129_commune_contour"),
    ]

    operations = [
        migrations.AddField(
            model_name="commune",
            name="arrondissement",
            field=models.BooleanField(
                default=False,
                help_text="Cette commune est un arrondissement (Paris, Lyon, Marseille)",
                verbose_name="Arrondissement",
            ),
        ),
        migrations.AddIndex(
            model_name="commune",
            index=models.Index(fields=["arrondissement"], name="erp_commune_arrondi_d4ff5c_idx"),
        ),
    ]
