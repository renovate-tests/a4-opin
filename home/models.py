from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import blocks as core_blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailembeds import blocks as embed_blocks
from wagtail.wagtailimages import blocks as image_blocks
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets import blocks as snippet_blocks
from wagtail.wagtailsnippets.models import register_snippet

from contrib.translations.translations import TranslatedField
from euth.projects import models as prj_models


# Snippets
from euth_wagtail.settings import LANGUAGES


class RSSImport(models.Model):
    url = models.URLField(null=True, blank=True)

    rss_title_en = models.CharField(max_length=255)
    rss_title_de = models.CharField(max_length=255, blank=True)
    rss_title_it = models.CharField(max_length=255, blank=True)
    rss_title_fr = models.CharField(max_length=255, blank=True)
    rss_title_sv = models.CharField(max_length=255, blank=True)
    rss_title_sl = models.CharField(max_length=255, blank=True)
    rss_title_da = models.CharField(max_length=255, blank=True)

    translated_rss_title = TranslatedField('rss_title')

    panels = [
        edit_handlers.FieldPanel('url'),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('rss_title_en'),
                edit_handlers.FieldPanel('rss_title_de'),
                edit_handlers.FieldPanel('rss_title_it'),
                edit_handlers.FieldPanel('rss_title_fr'),
                edit_handlers.FieldPanel('rss_title_sv'),
                edit_handlers.FieldPanel('rss_title_sl'),
                edit_handlers.FieldPanel('rss_title_da'),
            ],
            heading="Translations",
            classname="collapsible collapsed"
        )
    ]

    def __str__(self):
        return self.rss_title_en


class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+'
    )

    @property
    def link(self):
        return self.link_page.url

    panels = [
        edit_handlers.PageChooserPanel('link_page')
    ]

    class Meta:
        abstract = True


class MenuItem(LinkFields):
    menu_title_en = models.CharField(max_length=255)
    menu_title_de = models.CharField(max_length=255, blank=True)
    menu_title_it = models.CharField(max_length=255, blank=True)
    menu_title_fr = models.CharField(max_length=255, blank=True)
    menu_title_sv = models.CharField(max_length=255, blank=True)
    menu_title_sl = models.CharField(max_length=255, blank=True)
    menu_title_da = models.CharField(max_length=255, blank=True)

    translated_menu_title = TranslatedField('menu_title')

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('menu_title_en'),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('menu_title_de'),
                edit_handlers.FieldPanel('menu_title_it'),
                edit_handlers.FieldPanel('menu_title_fr'),
                edit_handlers.FieldPanel('menu_title_sv'),
                edit_handlers.FieldPanel('menu_title_sl'),
                edit_handlers.FieldPanel('menu_title_da'),
            ],
            heading="Translations",
            classname="collapsible collapsed"
        )] + LinkFields.panels


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('home.NavigationMenu', related_name='menu_items')


class NavigationMenu(ClusterableModel):

    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.menu_name


NavigationMenu.panels = [
    edit_handlers.FieldPanel('menu_name', classname='full title'),
    edit_handlers.InlinePanel('menu_items', label="Menu Items")
]

register_snippet(NavigationMenu)
register_snippet(RSSImport)


# Blocks
class RSSImportBlock(core_blocks.StructBlock):
    feed = snippet_blocks.SnippetChooserBlock(
        required=True, target_model=RSSImport)

    class Meta:
        template = 'home/blocks/rss_import_block.html'
        icon = 'snippet'
        label = 'RSS Import'


class InlineImageBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    internal_link = core_blocks.PageChooserBlock(required=False)
    external_link = core_blocks.URLBlock(required=False)
    link_text = core_blocks.TextBlock(required=False)


class InlineImagesBlock(core_blocks.StructBlock):

    inline_images = core_blocks.ListBlock(InlineImageBlock())
    columns = core_blocks.ChoiceBlock(choices=[
        ('4', 'three columns'),
        ('6', 'two columns'),
    ], icon='cup', required=False, help_text='')

    class Meta:
        template = 'home/blocks/inline_images_block.html'
        icon = 'placeholder'
        label = 'Inline Images Block'


class CallToActionBlock(core_blocks.StructBlock):
    internal_link = core_blocks.PageChooserBlock(required=False)
    external_link = core_blocks.URLBlock(required=False)
    link_text = core_blocks.TextBlock(required=False)


class InfoBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title", required=False)
    image = image_blocks.ImageChooserBlock(required=False)
    text = core_blocks.RichTextBlock(required=False)
    button = CallToActionBlock(required=False)
    highlight = core_blocks.ChoiceBlock(choices=[
        ('', 'None'),
        ('highlight', 'Highlight (blue)'),
        ('boxed', 'Boxed'),
        ('boxed2', 'Boxed Variation'),
        ('highlight-purple', 'Highlight (purple)')
    ], icon='cup',
        required=False,
        help_text='How should this block be displayed?'
    )
    alignment = core_blocks.ChoiceBlock(
        choices=[
            ('vertical', 'vertical'),
            ('horizontal', 'horizontal'),
        ],
        icon='cup',
        default='vertical',
        help_text='How should the text and image be aligned?'
    )

    class Meta:
        template = 'home/blocks/info_block.html'
        icon = 'placeholder'
        label = 'Info Block'


class ColumnBlock(core_blocks.StructBlock):
    title_col1 = core_blocks.CharBlock(classname="full title", required=False)
    image_col1 = image_blocks.ImageChooserBlock(required=False)
    text_col1 = core_blocks.RichTextBlock(required=False)

    title_col2 = core_blocks.CharBlock(classname="full title", required=False)
    image_col2 = image_blocks.ImageChooserBlock(required=False)
    text_col2 = core_blocks.RichTextBlock(required=False)

    title_col3 = core_blocks.CharBlock(classname="full title", required=False)
    image_col3 = image_blocks.ImageChooserBlock(required=False)
    text_col3 = core_blocks.RichTextBlock(required=False)

    class Meta:
        template = 'home/blocks/column_block.html'
        icon = 'placeholder'
        label = 'Column Block'


class VideoBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    video = embed_blocks.EmbedBlock()

    class Meta:
        template = 'home/blocks/video_block.html'
        icon = 'placeholder'
        label = 'Video Block'


class NewsBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    news = core_blocks.CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/news_block.html'
        icon = 'placeholder'
        label = 'News Block'


class WideImageBlock(core_blocks.StructBlock):

    image = image_blocks.ImageChooserBlock()

    class Meta:
        template = 'home/blocks/wide_image_block.html'
        icon = 'placeholder'
        label = 'Wide Image Block'


class ContactBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    name_label = core_blocks.CharBlock(classname="full title")
    email_label = core_blocks.CharBlock(classname="full title")
    subject_label = core_blocks.CharBlock(classname="full title")
    message_label = core_blocks.CharBlock(classname="full title")
    submit_label = core_blocks.CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/contact_block.html'
        icon = 'placeholder'
        label = 'Contact Block'


class AccordionItemBlock(core_blocks.StructBlock):
    title = core_blocks.TextBlock(required=False)
    content = core_blocks.RichTextBlock(required=False)


class AccordionBlock(core_blocks.StructBlock):

    accordion_items = core_blocks.ListBlock(AccordionItemBlock())

    class Meta:
        template = 'home/blocks/accordion_block.html'
        icon = 'placeholder'
        label = 'Accordion Block'


class ImageTextItemBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    text = core_blocks.TextBlock()


class ImageTextBlockList(core_blocks.StructBlock):

    imageTextBlockList = core_blocks.ListBlock(ImageTextItemBlock())

    class Meta:
        template = 'home/blocks/imageTextBlockList_block.html'
        icon = 'placeholder'
        label = 'Image Text Block'


def get_abstract_translated_page(block_types=None):
    block_types_set = block_types or [
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
        ('column_block', ColumnBlock()),
    ]

    class AbstractTranslatedPage(Page):
        class Meta:
            abstract = True

        def __init__(self):
            # Title
            self.translated_title = TranslatedField('title')
            for lang_code, lang in LANGUAGES:
                setattr(self,
                        'title_{}'.format(lang_code),
                        models.CharField(
                            max_length=255,
                            blank=True,
                            verbose_name="Header Title"
                        ))
            # Body
            self.body = TranslatedField('body')
            for lang_code, lang in LANGUAGES:
                setattr(self,
                        'body_{}'.format(lang_code),
                        StreamField(
                            block_types_set,
                            null=True,
                            blank=True
                        ))

        general_panels = [
            edit_handlers.FieldPanel('title', classname='title'),
            edit_handlers.FieldPanel('slug'),
        ]

        content_panels = [
            edit_handlers.MultiFieldPanel(
                [
                    edit_handlers.FieldPanel('title_' + lang_code),
                    edit_handlers.StreamFieldPanel('body_' + lang_code)
                ],
                heading=lang,
                classname="collapsible collapsed"
            ) for lang_code, lang in LANGUAGES
        ]

        edit_handler = edit_handlers.TabbedInterface([
            edit_handlers.ObjectList(content_panels, heading='Content'),
            edit_handlers.ObjectList(general_panels, heading='General')
        ])
    return AbstractTranslatedPage


# Pages
class HomePage:
    class Meta:
        verbose_name = "Homepage"

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image",
        help_text="The Image that is shown on top of the page"
    )

    videoplayer_url = models.URLField()

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('image'),
        edit_handlers.FieldPanel('videoplayer_url'),
    ]

    parent_page_types = []
    subpage_types = [
        'home.SimplePage',
    ]

    @property
    def featured_projects(self):
        return prj_models.Project.objects.featured()


class SimplePage:
    translated_intro = TranslatedField('intro')
    intro_en = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_de = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_it = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_fr = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_sv = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_sl = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_da = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")

    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Body
    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ]

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('intro_image')
    ]

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_' + lang_code),
                edit_handlers.FieldPanel('intro_' + lang_code),
                edit_handlers.StreamFieldPanel('body_' + lang_code)
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]


class ManualOverviewPage:
    block_types = [
        ('ingredients_list', core_blocks.ListBlock(core_blocks.StructBlock([
            ('ingredient', core_blocks.CharBlock(required=True)),
            ('amount', core_blocks.CharBlock()),
        ])))
    ]
