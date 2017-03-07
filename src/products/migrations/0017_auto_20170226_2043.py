# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='brands',
        ),
        migrations.AddField(
            model_name='category',
            name='brands',
            field=models.ManyToManyField(blank=True, to='products.Brand'),
        ),
    ]
