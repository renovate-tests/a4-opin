# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import ckeditor.fields
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('item_ptr', models.OneToOneField(to='euth_modules.Item', parent_link=True, serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('name', models.CharField(max_length=120)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='ideas/images', blank=True, validators=[euth.contrib.validators.validate_hero_image])),
            ],
            options={
                'abstract': False,
            },
            bases=('euth_modules.item',),
        ),
    ]
