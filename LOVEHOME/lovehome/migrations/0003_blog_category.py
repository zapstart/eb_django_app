# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0002_auto_20150609_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_category', models.CharField(max_length=50)),
            ],
        ),
    ]
