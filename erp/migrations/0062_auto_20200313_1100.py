# Generated by Django 3.0.4 on 2020-03-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0061_auto_20200312_1903"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessibilite",
            name="commentaire",
            field=models.TextField(
                blank=True,
                help_text="Indiquez tout autre information qui vous semble pertinente pour décrire l’accessibilité du bâtiment",
                max_length=1000,
                null=True,
                verbose_name="Commentaire libre",
            ),
        ),
        migrations.AlterField(
            model_name="accessibilite",
            name="cheminement_ext_retrecissement",
            field=models.BooleanField(
                blank=True,
                choices=[(True, "Oui"), (False, "Non"), (None, "Inconnu")],
                help_text="Existe-t-il un ou plusieurs rétrécissements (inférieur à 80 cm) du chemin emprunté par le public pour atteindre l'entrée ?",
                null=True,
                verbose_name="Rétrécissement du cheminement",
            ),
        ),
    ]
