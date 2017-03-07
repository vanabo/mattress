# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20170228_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='brands',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='categories',
            new_name='category',
        ),
    ]
