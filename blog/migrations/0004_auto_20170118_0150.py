# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170118_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='telephone',
            field=models.CharField(max_length=11),
        ),
    ]