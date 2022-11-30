# Generated by Django 3.0.4 on 2020-03-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0062_auto_20200313_1100"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessibilite",
            name="entree_vitree",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "Oui"), (False, "Non"), (None, "Inconnu")],
                help_text="La porte d'entrée est-elle vitrée ?",
                null=True,
                verbose_name="Entrée vitrée",
            ),
        ),
        migrations.AlterField(
            model_name="accessibilite",
            name="entree_reperage_vitres",
            field=models.BooleanField(
                blank=True,
                choices=[
                    (True, "Oui"),
                    (False, "Non"),
                    (None, "Inconnu ou sans objet"),
                ],
                help_text="Si l'entrée est vitrée, présence d'éléments contrastés permettant de visualiser l'entrée ?",
                null=True,
                verbose_name="Vitrophanie",
            ),
        ),
    ]
