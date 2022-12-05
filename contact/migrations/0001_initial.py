# Generated by Django 3.0.7 on 2020-09-08 13:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("erp", "0090_auto_20200908_1548"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "topic",
                    models.CharField(
                        choices=[
                            ("bug", "Rapport de bug"),
                            ("support", "Demande d'aide"),
                            ("contact", "Prise de contact"),
                            ("partenariat", "Proposition de partenariat"),
                            ("signalement", "Signalement d'un problème de données"),
                            ("autre", "Autre demande"),
                        ],
                        default="contact",
                        max_length=50,
                        verbose_name="Sujet",
                    ),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=255, null=True, verbose_name="Votre nom"),
                ),
                (
                    "email",
                    models.EmailField(max_length=255, verbose_name="Adresse email"),
                ),
                ("body", models.TextField(max_length=5000, verbose_name="Message")),
                ("sent_ok", models.BooleanField(verbose_name="Envoi OK")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date de création"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Dernière modification"),
                ),
                (
                    "erp",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="erp.Erp",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
        migrations.AddIndex(
            model_name="message",
            index=models.Index(fields=["topic"], name="contact_mes_topic_4a6e9c_idx"),
        ),
    ]
