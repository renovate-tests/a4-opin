import json

from django import forms
from django.core.exceptions import ValidationError

from . import widgets


class RichtextField(forms.Field):
    widget = widgets.Editor

    def to_python(self, value):
        try:
            return json.loads(value)
        except json.JSONDecoderError:
            raise ValidationError('Invalid input data.')


class TestForm(forms.Form):
    text = RichtextField(
        label="Text",
    )
