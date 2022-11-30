# Generated by Django 3.0.3 on 2020-02-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0025_auto_20200205_0839"),
    ]

    operations = [
        migrations.AddField(
            model_name="cheminement",
            name="aide_humaine",
            field=models.BooleanField(
                blank=True,
                help_text="Présence ou possibilité d'une aide humaine au déplacement",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="accessibilite",
            name="accueil_personnels",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inconnu"),
                    ("aucun", "Aucun personnel"),
                    ("formés", "Personnels sensibilisés et formés"),
                    ("non-formés", "Personnels non non-formés"),
                ],
                help_text="Présence et type de personnel d'accueil",
                max_length=255,
                null=True,
                verbose_name="Personnel d'accueil",
            ),
        ),
        migrations.AlterField(
            model_name="accessibilite",
            name="accueil_visibilite",
            field=models.BooleanField(
                blank=True,
                help_text="La zone d'accueil est-elle visible depuis l'entrée ?",
                null=True,
                verbose_name="Visibilité de la zone d'accueil",
            ),
        ),
        migrations.AlterField(
            model_name="accessibilite",
            name="entree_reperage",
            field=models.BooleanField(
                blank=True,
                help_text="Présence d'éléments de répérage de l'entrée",
                null=True,
                verbose_name="Repérage de l'entrée",
            ),
        ),
        migrations.AlterField(
            model_name="cheminement",
            name="devers",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inconnu"),
                    ("aucun", "Aucun"),
                    ("léger", "Léger"),
                    ("important", "Important"),
                ],
                help_text="Inclinaison transversale du cheminement",
                max_length=15,
                null=True,
                verbose_name="Dévers",
            ),
        ),
        migrations.AlterField(
            model_name="cheminement",
            name="escalier_reperage",
            field=models.BooleanField(
                blank=True,
                help_text="Si marches contrastées, bande d’éveil ou nez de marche contrastés, indiquez “Oui”",
                null=True,
                verbose_name="Repérage de l'escalier",
            ),
        ),
        migrations.AlterField(
            model_name="cheminement",
            name="pente",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inconnu"),
                    ("aucune", "Aucune"),
                    ("légère", "Légère"),
                    ("importante", "Importante"),
                ],
                help_text="Présence et type de pente",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="cheminement",
            name="rampe",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inconnu"),
                    ("aucune", "Aucune"),
                    ("fixe", "Fixe"),
                    ("amovible", "Amovible"),
                ],
                help_text="Présence et type de rampe",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="cheminement",
            name="type",
            field=models.CharField(
                choices=[
                    (
                        "stationnement_vers_erp",
                        "Cheminement depuis le stationnement de l'ERP",
                    ),
                    (
                        "stationnement_ext_vers_erp",
                        "Cheminement depuis le stationnement extérieur à l'ERP",
                    ),
                    (
                        "stationnement_vers_entree",
                        "Cheminement du stationnement à l'entrée du bâtiment",
                    ),
                    (
                        "parcelle_vers_entree",
                        "Cheminement depuis l'entrée de la parcelle de terrain à l'entrée du bâtiment",
                    ),
                    (
                        "entree_vers_accueil",
                        "Cheminement de l'entrée du bâtiment à la zone d'accueil",
                    ),
                    ("entree", "Cheminement autour de l'entrée"),
                ],
                default="entree",
                help_text="Type de cheminement",
                max_length=100,
                verbose_name="Cheminement",
            ),
        ),
    ]
