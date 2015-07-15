# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0006_auto_20150617_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_text',
            name='category',
        ),
    ]
