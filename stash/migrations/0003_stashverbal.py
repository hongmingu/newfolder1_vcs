# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 14:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stash', '0002_auto_20170621_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='StashVerbal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stashVerbalText', models.TextField(max_length=200)),
                ('stashCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('stashUpdatedAt', models.DateTimeField(auto_now=True)),
                ('stash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stash.Stash')),
                ('stashVerbalUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
