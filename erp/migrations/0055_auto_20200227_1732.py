# Generated by Django 3.0.3 on 2020-02-27 16:32

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0054_auto_20200227_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activite',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, help_text="Identifiant d'URL (slug)", populate_from='nom', unique=True),
        ),
        migrations.AlterField(
            model_name='cheminement',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, help_text="Identifiant d'URL (slug)", populate_from='nom', unique=True),
        ),
        migrations.AlterField(
            model_name='equipementmalentendant',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, help_text="Identifiant d'URL (slug)", populate_from='nom', unique=True),
        ),
        migrations.AlterField(
            model_name='erp',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, help_text="Identifiant d'URL (slug)", populate_from='nom', unique=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, help_text="Identifiant d'URL (slug)", populate_from='nom', unique=True),
        ),
    ]
