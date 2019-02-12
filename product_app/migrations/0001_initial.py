# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('parent_category_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'product',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='product_linking',
            field=models.ManyToManyField(to='product_app.Product'),
            preserve_default=True,
        ),
    ]
