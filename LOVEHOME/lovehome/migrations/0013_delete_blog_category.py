# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0012_remove_blog_text_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blog_category',
        ),
    ]
