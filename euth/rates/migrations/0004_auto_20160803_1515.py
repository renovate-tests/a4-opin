# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_rates', '0003_auto_20160803_1437'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('content_type', 'object_pk', 'user')]),
        ),
    ]