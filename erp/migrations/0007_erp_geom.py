# Generated by Django 3.0.2 on 2020-01-31 22:00

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0006_auto_20200131_1634"),
    ]

    operations = [
        migrations.AddField(
            model_name="erp",
            name="geom",
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
