# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20170306_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Material9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.ForeignKey(to='products.Material1', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material10',
            field=models.ForeignKey(to='products.Material10', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material2',
            field=models.ForeignKey(to='products.Material2', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material3',
            field=models.ForeignKey(to='products.Material3', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material4',
            field=models.ForeignKey(to='products.Material4', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material5',
            field=models.ForeignKey(to='products.Material5', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material6',
            field=models.ForeignKey(to='products.Material6', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material7',
            field=models.ForeignKey(to='products.Material7', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material8',
            field=models.ForeignKey(to='products.Material8', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='material9',
            field=models.ForeignKey(to='products.Material9', null=True, blank=True),
        ),
    ]
