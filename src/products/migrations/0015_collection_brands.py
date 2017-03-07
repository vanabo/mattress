# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='brands',
            field=models.ManyToManyField(blank=True, to='products.Brand'),
        ),
    ]
