# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0026_change_public_visibility_perm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='last_ping',
        ),
        migrations.AddField(
            model_name='judge',
            name='online',
            field=models.BooleanField(default=False, verbose_name='Judge online status'),
        ),
    ]
