# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyker_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraction',
            name='image_filename',
            field=models.CharField(default=b'\\userdata\no_user\x08lank.png', max_length=200),
        ),
    ]
