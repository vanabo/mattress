# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_categoryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to=products.models.image_upload_to_brand)),
                ('brand', models.ForeignKey(to='products.Brand')),
            ],
        ),
    ]
