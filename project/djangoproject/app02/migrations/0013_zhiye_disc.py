# Generated by Django 4.0.3 on 2022-08-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0012_disc_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='zhiye',
            name='disc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
