from rest_framework import mixins, viewsets

from adhocracy4.api.mixins import ModuleMixin
from adhocracy4.api.permissions import ViewSetRulesPermission

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      ModuleMixin,
                      viewsets.GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (ViewSetRulesPermission,)

    def get_permission_object(self):
        return self.module

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'module_pk': self.module_pk,
        })
        return context
