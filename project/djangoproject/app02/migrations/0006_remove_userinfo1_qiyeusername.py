# Generated by Django 3.2 on 2022-08-10 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0005_auto_20220810_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo1',
            name='qiyeusername',
        ),
    ]
