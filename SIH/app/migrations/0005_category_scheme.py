# Generated by Django 4.1 on 2022-08-13 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_profile_middle_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50)),
                ("desc", models.TextField(blank=True)),
                ("created_date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Scheme",
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
                ("name", models.CharField(max_length=50)),
                ("desc", models.TextField()),
                ("startDate", models.DateField()),
                ("endData", models.DateField()),
                ("img", models.ImageField(upload_to="")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.category"
                    ),
                ),
            ],
        ),
    ]
