# Generated by Django 3.1.5 on 2021-02-08 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0105_auto_20210203_1910'),
    ]

    operations = [
        migrations.RunSQL('update erp_accessibilite '
                          'set cheminement_ext_terrain_accidente = not cheminement_ext_terrain_accidente',
                          elidable=True)
    ]
