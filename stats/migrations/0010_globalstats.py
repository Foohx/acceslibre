# Generated by Django 3.2.13 on 2022-06-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0009_auto_20220616_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_singleton', models.BooleanField(default=True, editable=False, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('erp_counts_histogram', models.JSONField(default=dict)),
                ('stats_territoires_sort_count', models.JSONField(default=dict)),
                ('stats_territoires_sort_default', models.JSONField(default=dict)),
                ('top_contributors', models.JSONField(default=dict)),
            ],
            options={
                'verbose_name': 'Statistiques',
                'verbose_name_plural': 'Statistiques',
            },
        ),
    ]
