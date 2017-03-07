# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20170302_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='building',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='flat',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='house',
            field=models.CharField(max_length=10),
        ),
    ]
