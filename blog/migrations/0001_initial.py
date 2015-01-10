# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import core.mixins
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='title', editable=False, blank=True)),
                ('body', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('edited_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
            bases=(core.mixins.MarkdownMixin, models.Model),
        ),
    ]
