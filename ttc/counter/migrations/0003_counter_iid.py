# Generated by Django 3.1.7 on 2021-06-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_auto_20210628_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='iid',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
