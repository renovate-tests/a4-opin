from django import forms
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.safestring import mark_safe


class Editor(forms.Textarea):

    def use_required_attribute(self, *args):
        return False

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = {
            'class': 'richtext',
            'style': 'background: #f3f3f3; border: 1px solid #d8d8d8;'
        }

        if attrs:
            final_attrs.update(attrs)

        html = [
            '<div{!s}>{!s}</div>'.format(flatatt(final_attrs), escape(value)),
            '<input type="hidden" name="{}"></input>'.format(name)
        ]
        return mark_safe('\n'.join(html))

    @property
    def media(self):
        return forms.Media(
            css={
                'all': [
                    # FIXME: should not be loaded from CDN
                    '//cdn.quilljs.com/1.3.2/quill.snow.css',
                    (
                        '//cdnjs.cloudflare.com/ajax/libs/'
                        'twitter-bootstrap/3.3.7/css/bootstrap.min.css'
                    ),
                    'richtexts/editor.css',
                ],
            },
            js=[
                # FIXME: should not be loaded from CDN
                '//code.jquery.com/jquery-3.2.1.min.js',
                '//cdn.quilljs.com/1.3.2/quill.js',
                (
                    'https://cdnjs.cloudflare.com/ajax/libs/'
                    'twitter-bootstrap/3.3.7/js/bootstrap.min.js'
                ),

                'richtexts/modal-workflow.js',
                'richtexts/editor.js',
            ])
