# Generated by Django 3.2.11 on 2022-05-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0006_manual_implementation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="implementation",
            name="urlpath",
            field=models.URLField(help_text="Url complète", unique=True),
        ),
        migrations.AlterField(
            model_name="referer",
            name="domain",
            field=models.URLField(
                help_text="Domaine du site réutilisateur", unique=True
            ),
        ),
    ]
