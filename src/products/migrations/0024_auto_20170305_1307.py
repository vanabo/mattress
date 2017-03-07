# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20170302_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardness',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=120)),
                ('description', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hardness',
            field=models.ManyToManyField(blank=True, to='products.Hardness'),
        ),
    ]
