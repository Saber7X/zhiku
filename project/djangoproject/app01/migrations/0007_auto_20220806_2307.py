# Generated by Django 3.2 on 2022-08-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20220731_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='qiyeuser',
            name='cltime',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='fjob',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='http',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='jbjs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='qygm',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='rzzt',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qiyeuser',
            name='zjob',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
