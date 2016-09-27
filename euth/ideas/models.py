from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.functional import cached_property

from contrib.transforms import html_transforms
from euth.comments import models as comment_models
from euth.contrib import validators
from euth.modules import models as module_models
from euth.ratings import models as rating_models


class Idea(module_models.Item):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=120)
    description = RichTextField()
    image = models.ImageField(upload_to='ideas/images', blank=True,
                              validators=[validators.validate_idea_image])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.description = html_transforms.clean_html_field(
            self.description)
        super(Idea, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('idea-detail', args=[str(self.slug)])

    @cached_property
    def comments(self):
        contenttype = ContentType.objects.get_for_model(self)
        pk = self.id
        comments = comment_models.Comment.objects.all().filter(
            content_type=contenttype, object_pk=pk)
        return comments

    @cached_property
    def negative_ratings(self):
        contenttype = ContentType.objects.get_for_model(self)
        pk = self.id
        negative_ratings = rating_models.Rating.objects.all().filter(
            content_type=contenttype, object_pk=pk, value=-1).count()
        return negative_ratings

    @cached_property
    def positive_ratings(self):
        contenttype = ContentType.objects.get_for_model(self)
        pk = self.id
        positive_ratings = rating_models.Rating.objects.all().filter(
            content_type=contenttype, object_pk=pk, value=1).count()
        return positive_ratings
