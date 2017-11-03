# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20170629_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='optica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='services.Optica', verbose_name='Óptica'),
        ),
    ]