# Generated by Django 3.1.3 on 2020-11-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0099_activite_vector_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='statuscheck',
            name='non_diffusable',
            field=models.BooleanField(default=False, verbose_name='Données SIRENE non diffusables'),
        ),
    ]
