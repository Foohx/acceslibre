# Generated by Django 3.2.1 on 2021-06-14 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailToken",
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
                ("activation_token", models.UUIDField()),
                ("new_email", models.EmailField(max_length=254)),
                ("expire_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Utilisateur",
                    ),
                ),
            ],
            options={
                "verbose_name": "EmailToken",
                "verbose_name_plural": "EmailTokens",
                "ordering": ("-created_at",),
            },
        ),
        migrations.AddIndex(
            model_name="emailtoken",
            index=models.Index(
                fields=["activation_token"], name="compte_emai_activat_10bf8e_idx"
            ),
        ),
    ]
