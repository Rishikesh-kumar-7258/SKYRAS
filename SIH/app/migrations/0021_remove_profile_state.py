# Generated by Django 4.1 on 2022-08-26 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0020_profile_email_token_profile_is_verified_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="state",),
    ]