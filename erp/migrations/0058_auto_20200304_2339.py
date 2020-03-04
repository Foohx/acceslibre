# Generated by Django 3.0.3 on 2020-03-04 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0057_erp_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erp',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Créateur'),
        ),
        migrations.AddIndex(
            model_name='erp',
            index=models.Index(fields=['commune'], name='erp_erp_commune_310ef8_idx'),
        ),
    ]
