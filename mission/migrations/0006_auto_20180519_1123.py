# Generated by Django 2.0.2 on 2018-05-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0005_auto_20180519_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendrier',
            name='desc',
        ),
        migrations.AlterField(
            model_name='calendrier',
            name='title',
            field=models.CharField(default='10h - 20h', max_length=64),
        ),
    ]
