# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170226_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(to='products.Category', null=True, related_name='default_category', blank=True),
        ),
    ]
