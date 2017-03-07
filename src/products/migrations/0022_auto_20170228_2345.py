# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20170228_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brands',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='collections',
            new_name='collection',
        ),
    ]
