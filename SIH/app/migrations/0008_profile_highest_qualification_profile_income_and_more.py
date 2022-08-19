# Generated by Django 4.1 on 2022-08-19 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_scheme_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="highest_qualification",
            field=models.CharField(default="Matriculation", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="income",
            field=models.IntegerField(default=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="occupation",
            field=models.CharField(default="Farmer", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="sector",
            field=models.CharField(default="Agriculture", max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Eligibility",
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
                ("state", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=50)),
                ("age_start", models.IntegerField()),
                ("age_end", models.IntegerField()),
                ("category", models.CharField(max_length=50)),
                ("income_start", models.IntegerField()),
                ("income_end", models.IntegerField()),
                ("gender", models.CharField(max_length=50)),
                ("occupation", models.CharField(max_length=50)),
                ("qualification", models.CharField(max_length=50)),
                ("created_date", models.DateField(auto_now=True)),
                (
                    "scheme",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app.scheme"
                    ),
                ),
            ],
        ),
    ]
