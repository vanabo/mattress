# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20170226_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='type',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='building',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='flat',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddress',
            name='house',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_total_price',
            field=models.DecimalField(default=500, max_digits=50, decimal_places=2),
        ),
    ]
