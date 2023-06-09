# Generated by Django 4.2.1 on 2023-06-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetailTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=80, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=80, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=80, verbose_name='Email')),
                ('phoneNumber', models.IntegerField(verbose_name='Phone Number')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
            ],
        ),
    ]
