from django.conf import settings
from django.db import models
from model_utils import models as model_utils

from euth.projects import models as project_models


class Module(models.Model):
    name = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(max_length=512, unique=True)
    description = models.TextField
    weight = models.PositiveIntegerField()
    project = models.ForeignKey(
        project_models.Project, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.project, self.weight)


class Item(model_utils.TimeStampedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)