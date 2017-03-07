# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to_collection)),
                ('product', models.ForeignKey(to='products.Collection')),
            ],
        ),
    ]
