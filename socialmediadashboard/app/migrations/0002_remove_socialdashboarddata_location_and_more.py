# Generated by Django 4.1.3 on 2022-11-18 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialdashboarddata',
            name='location',
        ),
        migrations.RemoveField(
            model_name='socialdashboarddata',
            name='title',
        ),
    ]
