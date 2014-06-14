# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.mixins


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(core.mixins.MarkdownMixin, models.Model),
        ),
    ]
