# Generated by Django 3.2 on 2022-08-10 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0008_auto_20220810_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rencai',
            name='address',
        ),
        migrations.RemoveField(
            model_name='rencai',
            name='age',
        ),
        migrations.RemoveField(
            model_name='rencai',
            name='gender',
        ),
    ]
