from django import template

from .. import models

register = template.Library()


@register.assignment_tag()
def is_following(user, project):
    return models.Follow.objects.filter(
        enabled=True,
        project=project,
        creator=user
    ).exists()