# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20170305_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filler',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sofa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spring',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hardness',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=0, default=2, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='product',
            name='child',
            field=models.ManyToManyField(blank=True, to='products.Child'),
        ),
        migrations.AddField(
            model_name='product',
            name='filler',
            field=models.ManyToManyField(blank=True, to='products.Filler'),
        ),
        migrations.AddField(
            model_name='product',
            name='sofa',
            field=models.ManyToManyField(blank=True, to='products.Sofa'),
        ),
        migrations.AddField(
            model_name='product',
            name='spring',
            field=models.ManyToManyField(blank=True, to='products.Spring'),
        ),
    ]
