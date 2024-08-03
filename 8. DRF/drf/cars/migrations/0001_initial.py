# Generated by Django 4.1.10 on 2023-08-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("brand", models.CharField(max_length=60)),
                ("mark", models.CharField(max_length=60)),
                ("year", models.IntegerField()),
                ("price_usd", models.IntegerField()),
            ],
        ),
    ]