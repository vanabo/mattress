# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_collectionimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionimage',
            old_name='product',
            new_name='collection',
        ),
    ]
