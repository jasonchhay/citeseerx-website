# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0020_auto_20180627_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'teammember',
            name=b'image',
            field=models.FileField(help_text='', upload_to=b'team_portraits', default=b'noimage.png'),
        ),
    ]
