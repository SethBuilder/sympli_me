# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sympli', '0002_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
