# Generated by Django 3.2 on 2022-07-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zhiwei',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('xingzhi', models.CharField(blank=True, max_length=200, null=True)),
                ('describe', models.CharField(blank=True, max_length=200, null=True)),
                ('leibie', models.CharField(blank=True, max_length=200, null=True)),
                ('yaoqiu', models.CharField(blank=True, max_length=200, null=True)),
                ('xueli', models.CharField(blank=True, max_length=200, null=True)),
                ('key', models.CharField(blank=True, max_length=200, null=True)),
                ('fuli', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('xinzi', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
