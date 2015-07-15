# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0005_blog_text_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_text',
            name='category',
            field=models.ForeignKey(to='lovehome.blog_category', null=True, default=None),
        ),
    ]
