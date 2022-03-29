# Generated by Django 4.0.3 on 2022-03-29 07:06

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_users', models.IntegerField()),
                ('total_amount_paid', models.BigIntegerField()),
                ('total_users_benefited', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Statistics',
                'verbose_name_plural': 'Statistics',
            },
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('eligible_genders', models.CharField(choices=[('1', 'MALE'), ('2', 'FEMALE'), ('3', 'OTHER')], max_length=20)),
                ('eligible_category', models.CharField(choices=[('1', 'GENERAL'), ('2', 'OBC'), ('3', 'SC'), ('4', 'ST'), ('5', 'EWS')], max_length=20)),
                ('min_annual_income', models.BigIntegerField()),
                ('max_annual_income', models.BigIntegerField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('min_family_members', models.IntegerField()),
                ('max_family_members', models.IntegerField()),
                ('eligible_states', models.CharField(max_length=20)),
                ('eligible_districts', models.CharField(max_length=20)),
                ('eligible_cities', models.CharField(max_length=20)),
                ('eligible_pincodes', models.CharField(max_length=20)),
                ('stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.statistics')),
            ],
            options={
                'verbose_name': 'Scheme',
                'verbose_name_plural': 'Schemes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('pin_code', models.CharField(blank=True, max_length=50)),
                ('district', models.CharField(blank=True, max_length=50)),
                ('aadhar_number', models.BigIntegerField()),
                ('gender', models.CharField(choices=[('1', 'MALE'), ('2', 'FEMALE'), ('3', 'OTHER')], max_length=20)),
                ('dob', models.DateField()),
                ('category', models.CharField(choices=[('1', 'GENERAL'), ('2', 'OBC'), ('3', 'SC'), ('4', 'ST'), ('5', 'EWS')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]