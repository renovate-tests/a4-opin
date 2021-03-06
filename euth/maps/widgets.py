from django.conf import settings
from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe


class MapChoosePolygonWidget(Widget):

    class Media:
        js = (
            'leaflet.js',
            'leaflet.draw.js',
            'js/custom/map_choose_polygon.js',
        )
        css = {'all': (
            'leaflet.css',
            'leaflet.draw.css',
        )}

    def render(self, name, value, attrs, renderer=None):

        context = {
            'map_url': settings.BASE_MAP,
            'bbox': settings.MAP_BOUNDING_BOX,
            'name': name,
            'polygon': value
        }

        return mark_safe(
            loader.render_to_string(
                'euth_maps/map_choose_polygon_widget.html',
                context
            )
        )


class MapChoosePointWidget(Widget):

    def __init__(self, polygon, attrs=None):
        self.polygon = polygon
        super().__init__(attrs)

    class Media:
        js = ('leaflet.js',
              'js/custom/map_choose_point.js',
              )
        css = {'all': [
            'leaflet.css',
        ]}

    def render(self, name, value, attrs, renderer=None):

        context = {
            'map_url': settings.BASE_MAP,
            'bbox': settings.MAP_BOUNDING_BOX,
            'name': name,
            'point': value,
            'polygon': self.polygon
        }

        return mark_safe(
            loader.render_to_string(
                'euth_maps/map_choose_point_widget.html',
                context
            )
        )
