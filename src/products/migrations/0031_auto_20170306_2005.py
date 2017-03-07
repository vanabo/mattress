# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20170306_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(null=True, blank=True, to='products.Material'),
        ),
    ]
