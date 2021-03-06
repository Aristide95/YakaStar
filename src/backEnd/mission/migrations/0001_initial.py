# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-03 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAuthUsersocialauth',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('provider', models.CharField(max_length=32)),
                ('user_id', models.CharField(max_length=255)),
                ('uid', models.CharField(max_length=255)),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'social_auth_usersocialauth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Calendrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('status', models.CharField(max_length=64)),
                ('cv_url', models.URLField(null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('desc', models.TextField()),
                ('type_mission', models.CharField(max_length=64)),
                ('state', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publication_date', models.DateTimeField(null=True)),
                ('client_name', models.CharField(max_length=64)),
                ('logo_url', models.URLField(null=True)),
                ('devis_url', models.URLField(null=True)),
                ('num_presta', models.IntegerField(default=1)),
                ('commercial_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mission.Etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Techno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='techno',
            field=models.ManyToManyField(to='mission.Techno'),
        ),
    ]
