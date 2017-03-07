# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20170306_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='child',
        ),
        migrations.AddField(
            model_name='product',
            name='child',
            field=models.ForeignKey(to='products.Child', blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='filler',
        ),
        migrations.AddField(
            model_name='product',
            name='filler',
            field=models.ForeignKey(to='products.Filler', blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='hardness',
        ),
        migrations.AddField(
            model_name='product',
            name='hardness',
            field=models.ForeignKey(to='products.Hardness', blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='sofa',
        ),
        migrations.AddField(
            model_name='product',
            name='sofa',
            field=models.ForeignKey(to='products.Sofa', blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='spring',
        ),
        migrations.AddField(
            model_name='product',
            name='spring',
            field=models.ForeignKey(to='products.Spring', blank=True, null=True),
        ),
    ]
