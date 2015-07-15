# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0016_blog_text_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_text',
            old_name='category',
            new_name='time_category',
        ),
    ]
