# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0017_auto_20150618_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_text',
            name='time_category',
        ),
    ]
