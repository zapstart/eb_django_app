# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lovehome', '0013_delete_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_category', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog_text',
            name='blog_content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='blog_text',
            name='category',
            field=models.ForeignKey(to='lovehome.blog_category', null=True),
        ),
    ]
