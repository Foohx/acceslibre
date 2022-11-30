# Generated by Django 3.2 on 2021-04-19 11:09

from django.db import migrations, models

from erp import schema


def migrate_value(previous_value):
    if previous_value == schema.PENTE_AUCUNE:
        return False, schema.PENTE_AUCUNE
    elif previous_value == schema.PENTE_LEGERE:
        return True, schema.PENTE_LEGERE
    elif previous_value == schema.PENTE_IMPORTANTE:
        return True, schema.PENTE_IMPORTANTE
    else:
        return None, None


def migrate_previous_data(apps, schema_editor):
    Accessibilite = apps.get_model("erp", "Accessibilite")
    for a in Accessibilite.objects.all():
        (presence, degre_difficulte) = migrate_value(a.cheminement_ext_pente)
        a.cheminement_ext_pente_presence = presence
        a.cheminement_ext_pente_degre_difficulte = degre_difficulte
        a.save()


class Migration(migrations.Migration):
    dependencies = [
        ("erp", "0115_auto_20210419_1033"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessibilite",
            name="cheminement_ext_pente_presence",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "Oui"), (False, "Non"), (None, "Inconnu")],
                null=True,
                verbose_name="Pente présence",
            ),
        ),
        migrations.AddField(
            model_name="accessibilite",
            name="cheminement_ext_pente_degre_difficulte",
            field=models.CharField(
                blank=True,
                choices=[
                    ("aucune", "Aucune"),
                    ("légère", "Légère"),
                    ("importante", "Importante"),
                    (None, "Inconnu"),
                ],
                max_length=15,
                null=True,
                verbose_name="Difficulté de la pente",
            ),
        ),
        migrations.AddField(
            model_name="accessibilite",
            name="cheminement_ext_pente_longueur",
            field=models.CharField(
                blank=True,
                choices=[
                    ("courte", "< 0,5m"),
                    ("moyenne", "entre 0,5 et 2m"),
                    ("longue", "> 2m"),
                    (None, "Inconnu"),
                ],
                max_length=15,
                null=True,
                verbose_name="Longueur de la pente",
            ),
        ),
        migrations.RunPython(migrate_previous_data),
        migrations.RemoveField(
            model_name="accessibilite",
            name="cheminement_ext_pente",
        ),
    ]
