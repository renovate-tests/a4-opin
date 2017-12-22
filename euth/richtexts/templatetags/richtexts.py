from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_richtext(value):
    output = []

    for op in value['ops']:
        if 'a4image' in op['insert']:
            a4image = op['insert']['a4image']
            if a4image['style']:
                classes = 'image image-{}'.format(a4image['style'])
            else:
                classes = 'image image-default'

            output.append(format_html(
                '<img src="{}" alt="{}" class="{}">',
                a4image['url'],
                a4image['alt'],
                classes
            ))
        else:
            attributes = op.get('attribtues') or {}
            content = escape(op['insert']).replace('\n', '<br>\n')
            if 'italic' in attributes:
                content = '<i>{}</i>'.format(
                    content
                )
            elif 'bold' in attributes:
                content = '<b>{}</b>'.format(
                    content
                )
            output.append(content)

    # TODO: ensure everthing is escaped eg. use templates here
    return mark_safe(''.join(output))
