# Generated by Django 3.1.1 on 2020-10-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0094_auto_20201012_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erp',
            name='source',
            field=models.CharField(choices=[('admin', 'Back-office'), ('api', 'API'), ('entreprise_api', 'API Entreprise (publique)'), ('cconforme', 'cconforme'), ('public', 'Saisie manuelle publique'), ('public_erp', 'API des établissements publics'), ('sirene', 'API Sirene INSEE')], default='public', help_text='Nom de la source de données dont est issu cet ERP', max_length=100, null=True, verbose_name='Source'),
        ),
    ]
