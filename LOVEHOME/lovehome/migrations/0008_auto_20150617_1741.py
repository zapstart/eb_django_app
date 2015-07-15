# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0007_remove_blog_text_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_category',
            name='b_category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blog_text',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
