# Generated by Django 3.0.7 on 2020-06-29 10:13

from django.contrib.admin.models import LogEntry
from django.db import migrations, models


def migrate_sources(apps, schema_editor):
    Erp = apps.get_model("erp", "ERP")
    for erp in Erp.objects.filter(source="access4all"):
        try:
            LogEntry.objects.get(content_type__model="erp", object_id=erp.pk)
            erp.source = "admin"
        except (LogEntry.DoesNotExist):
            erp.source = "public"
        except LogEntry.MultipleObjectsReturned:
            erp.source = "admin"
        erp.save()
        print(f"Updated source for Erp {erp.nom}: {erp.source}")


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0080_auto_20200615_1757"),
    ]

    operations = [
        migrations.AlterField(
            model_name="erp",
            name="source",
            field=models.CharField(
                choices=[
                    ("admin", "Back-office"),
                    ("api", "API"),
                    ("public", "Application publique"),
                    ("cconforme", "cconforme"),
                ],
                default="public",
                help_text="Nom de la source de données dont est issu cet ERP",
                max_length=100,
                null=True,
                verbose_name="Source",
            ),
        ),
        migrations.RunPython(migrate_sources),
    ]
