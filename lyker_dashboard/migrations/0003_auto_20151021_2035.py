# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyker_dashboard', '0002_useraction_image_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='image_filename',
            field=models.CharField(default=b'/userdata/no_user/blank.png', max_length=200),
        ),
    ]
