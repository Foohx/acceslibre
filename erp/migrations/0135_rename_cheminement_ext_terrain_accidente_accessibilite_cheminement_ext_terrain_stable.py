# Generated by Django 3.2.5 on 2022-03-29 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0134_auto_20220328_1229"),
    ]

    operations = [
        migrations.RenameField(
            model_name="accessibilite",
            old_name="cheminement_ext_terrain_accidente",
            new_name="cheminement_ext_terrain_stable",
        ),
    ]
