# Generated by Django 3.2.5 on 2022-03-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0131_auto_20210628_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessibilite',
            name='sanitaires_adaptes_booltemp',
            field=models.BooleanField(blank=True, choices=[(True, 'Oui'), (False, 'Non'), (None, 'Inconnu')], null=True, verbose_name='Nombre de sanitaires adaptés'),
        ),
        migrations.AlterField(
            model_name='erp',
            name='source',
            field=models.CharField(choices=[('acceslibre', 'Base de données Acceslibre'), ('admin', 'Back-office'), ('api', 'API'), ('entreprise_api', 'API Entreprise (publique)'), ('cconforme', 'cconforme'), ('gendarmerie', 'Gendarmerie'), ('nestenn', 'Nestenn'), ('opendatasoft', 'API OpenDataSoft'), ('public', 'Saisie manuelle publique'), ('public_erp', 'API des établissements publics'), ('service_public', 'Service Public'), ('sirene', 'API Sirene INSEE'), ('tourisme-handicap', 'Tourisme & Handicap'), ('centres-vaccination', 'Centres de vaccination')], default='public', help_text='Nom de la source de données dont est issu cet ERP', max_length=100, null=True, verbose_name='Source'),
        ),
    ]
