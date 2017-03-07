# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_brandimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ManyToManyField(to='products.Brand', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category', blank=True),
        ),
    ]
