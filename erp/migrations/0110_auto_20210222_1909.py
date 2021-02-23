# Generated by Django 3.1.5 on 2021-02-22 18:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0109_accessibilite_entree_dispositif_appel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessibilite',
            name='entree_dispositif_appel_type',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('bouton', 'Bouton d’appel'), ('sonnette', 'Sonnette'), ('interphone', 'Interphone'), ('visiophone', 'Visiophone')], max_length=255), blank=True, default=list, null=True, size=None, verbose_name="Dispositifs d'appel disponibles"),
        ),
    ]
