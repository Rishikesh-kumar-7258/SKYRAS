# Generated by Django 4.1 on 2022-08-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_remove_document_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="name",
            field=models.CharField(
                choices=[
                    ("Aadhar", "Aadhar"),
                    ("Passport", "Passport"),
                    ("Voter ID", "Voter ID"),
                    ("Driving License", "Driving License"),
                    ("Pan Card", "Pan Card"),
                    ("Ration Card", "Ration Card"),
                    ("Passport", "Passport"),
                    ("Other", "Other"),
                ],
                max_length=100,
            ),
        ),
    ]
