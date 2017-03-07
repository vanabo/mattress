# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20170305_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.ManyToManyField(blank=True, to='products.Height'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.ManyToManyField(blank=True, to='products.Weight'),
        ),
    ]
