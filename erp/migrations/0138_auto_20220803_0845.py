# Generated by Django 3.2.13 on 2022-08-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0137_auto_20220725_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='activite',
            name='position',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Position dans la liste'),
        ),
        migrations.AlterField(
            model_name='accessibilite',
            name='entree_porte_presence',
            field=models.BooleanField(blank=True, choices=[(True, 'Oui'), (False, 'Non')], null=True, verbose_name='Y a-t-il une porte ?'),
        ),
        migrations.AlterField(
            model_name='erp',
            name='source',
            field=models.CharField(choices=[('acceslibre', 'Base de données Acceslibre'), ('admin', 'Back-office'), ('api', 'API'), ('entreprise_api', 'API Entreprise (publique)'), ('cconforme', 'cconforme'), ('gendarmerie', 'Gendarmerie'), ('nestenn', 'Nestenn'), ('opendatasoft', 'API OpenDataSoft'), ('public', 'Saisie manuelle publique'), ('public_erp', 'API des établissements publics'), ('sap', 'Sortir À Pair'), ('service_public', 'Service Public'), ('sirene', 'API Sirene INSEE'), ('tourisme-handicap', 'Tourisme & Handicap'), ('typeform', 'Questionnaires Typeform'), ('centres-vaccination', 'Centres de vaccination')], default='public', help_text='Nom de la source de données dont est issu cet ERP', max_length=100, null=True, verbose_name='Source'),
        ),
    ]
