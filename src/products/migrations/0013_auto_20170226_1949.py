# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170226_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='collections',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='default',
        ),
        migrations.AddField(
            model_name='collection',
            name='categories',
            field=models.ManyToManyField(to='products.Category', blank=True),
        ),
    ]
