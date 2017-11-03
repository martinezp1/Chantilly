# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20170629_1957'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='storehouse',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='optica',
        ),
        migrations.RemoveField(
            model_name='storehouse',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(null=True, verbose_name='Stock'),
        ),
        migrations.DeleteModel(
            name='StoreHouse',
        ),
    ]