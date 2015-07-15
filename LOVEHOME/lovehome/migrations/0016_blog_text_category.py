# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0015_auto_20150618_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_text',
            name='category',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]
