# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 10:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161223_1013'),
    ]

    operations = [
    ]

    if settings.PINAX_BLOG_SCOPING_MODEL is not None:
        dependencies.append(
            migrations.swappable_dependency(settings.PINAX_BLOG_SCOPING_MODEL)
        )

        operations.append(
            migrations.AddField(
                model_name='blog',
                name='scoper',
                field=models.OneToOneField(related_name='blog', to=settings.PINAX_BLOG_SCOPING_MODEL)
            )
        )
