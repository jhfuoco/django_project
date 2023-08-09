# Generated by Django 4.1 on 2023-08-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pybo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadImage",
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
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]