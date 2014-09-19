# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vin', models.CharField(max_length=17)),
                ('stock_number', models.CharField(max_length=5)),
                ('first_seen', models.DateTimeField(auto_now_add=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('year', models.IntegerField(max_length=4)),
                ('mileage', models.IntegerField(max_length=6)),
                ('transmission', models.CharField(max_length=30)),
                ('ex_color', models.CharField(max_length=80)),
                ('in_color', models.CharField(max_length=80)),
                ('engine', models.CharField(max_length=80)),
                ('url', models.URLField()),
                ('location', models.CharField(max_length=10)),
                ('trim', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feature', models.CharField(max_length=80)),
                ('car', models.ForeignKey(to='carter_scraper.Car')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(max_length=5)),
                ('car', models.ForeignKey(to='carter_scraper.Car')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
