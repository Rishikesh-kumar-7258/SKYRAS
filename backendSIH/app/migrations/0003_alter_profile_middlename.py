# Generated by Django 3.2.5 on 2022-08-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220803_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='middleName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
