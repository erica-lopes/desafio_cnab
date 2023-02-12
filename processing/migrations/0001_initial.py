# Generated by Django 4.1.5 on 2023-02-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=1)),
                ("date", models.DateField()),
                ("value", models.FloatField()),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.TimeField(max_length=6)),
                ("owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
            ],
        ),
    ]
