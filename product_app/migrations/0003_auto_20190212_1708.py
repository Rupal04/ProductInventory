# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_linking',
            new_name='product',
        ),
    ]
