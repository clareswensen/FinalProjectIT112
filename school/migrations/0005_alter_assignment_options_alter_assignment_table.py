# Generated by Django 4.0.5 on 2022-06-08 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_courseassignment_assignment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'verbose_name_plural': 'assignments'},
        ),
        migrations.AlterModelTable(
            name='assignment',
            table='assignment',
        ),
    ]