# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
    ]
