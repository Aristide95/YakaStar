# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-03 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mission.SocialAuthUsersocialauth'),
            preserve_default=False,
        ),
    ]