# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20170305_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.DecimalField(max_digits=20, decimal_places=1),
        ),
    ]
