from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        '^test',
        views.TestView.as_view(),
        name='test_editor',
    ),
    url(
        '^uploadimage',
        views.ImageUploadView.as_view(),
        name='upload_image',
    ),
]
