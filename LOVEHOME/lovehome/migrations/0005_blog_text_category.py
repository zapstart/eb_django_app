# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0004_auto_20150617_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_text',
            name='category',
            field=models.ForeignKey(default=None, to='lovehome.blog_category'),
        ),
    ]
