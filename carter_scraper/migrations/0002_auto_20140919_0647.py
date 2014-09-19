# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carter_scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='ex_color',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='in_color',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='location',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(max_length=6, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='number',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='stock_number',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='trim',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='vin',
            field=models.CharField(max_length=17, blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(max_length=5, blank=True),
        ),
    ]
