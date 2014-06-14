# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.mixins


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False)),
                ('body', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(core.mixins.MarkdownMixin, models.Model),
        ),
    ]
