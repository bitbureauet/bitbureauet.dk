# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('twitter_handle', models.CharField(blank=True, null=True, max_length=50)),
                ('on_call', models.BooleanField(editable=False, default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
