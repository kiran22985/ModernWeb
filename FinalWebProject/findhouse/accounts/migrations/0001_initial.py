# Generated by Django 3.1.3 on 2021-04-08 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('Email', models.EmailField(max_length=254, null=True, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('Phone', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)])),
                ('Username', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Confirm_password', models.CharField(max_length=200)),
            ],
        ),
    ]
