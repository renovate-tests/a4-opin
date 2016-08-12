from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from euth.contrib.base_models import TimeStampedModel


class Report(TimeStampedModel):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type", fk_field="object_pk")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)

    class Meta:
        unique_together = (('content_type', 'object_pk', 'user'))

    def __str__(self):
        return str(self.content_type) + '_' + str(self.object_pk)
