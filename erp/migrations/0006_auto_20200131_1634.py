# Generated by Django 3.0.2 on 2020-01-31 15:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0005_auto_20200131_1614"),
    ]

    operations = [
        migrations.AddField(
            model_name="activite",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="activite",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="erp",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="erp",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
