# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import django.db.models.deletion
import wagtail.wagtailimages.blocks
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('home', '0004_auto_20160121_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='+', blank=True, to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('background_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.wagtailcore.blocks.TextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('internal_link', wagtail.wagtailcore.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(max_length=255),
        ),
    ]
