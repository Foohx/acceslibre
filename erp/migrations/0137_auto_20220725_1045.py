# Generated by Django 3.2.13 on 2022-07-25 08:45
import datetime

from django.core.management import call_command
from django.db import migrations
from django.db.migrations import RunPython



def reset_user(apps, schema_editor):
    count = 0
    Erp = apps.get_model("erp", "Erp")
    qs = Erp.objects.filter(
        updated_at__gte=datetime.date(2022, 7, 5), accessibilite__isnull=False
    )
    print(f"{ qs.count()} erps sur la période")
    for erp in qs:
        try:
            if erp.user and erp.get_history() and erp.user != erp.get_first_user():
                if erp.get_first_user() is None and erp.user is not None:
                    pass
                else:
                    print(
                        f"{erp.pk} Changement de contributeur : {erp.user} -> {erp.get_first_user()}"
                    )
                    erp.user = erp.get_first_user()
                    erp.save()
                    count += 1
        except Exception as e:
            print(e)

    print(f"{count} erps mis à jour")


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0136_auto_20220516_1502"),
    ]

    operations = [RunPython(reset_user)]
