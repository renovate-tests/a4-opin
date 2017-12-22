from django.http import JsonResponse
from django.shortcuts import render
# from django.template import loader
from django.views import generic

from . import forms


class TestView(generic.FormView):
    form_class = forms.TestForm
    template_name = 'richtexts/form.html'

    def form_valid(self, form):
        return render(self.request, 'richtexts/valid.html', form.cleaned_data)


class ImageUploadView(generic.View):

    def post(self, request, **kwargs):
        return JsonResponse({
            'imageChosen': {
                'alt': 'Dogo',
                'url': 'https://i.imgur.com/GBerpnx.jpg',
                'style': 'centered'
            }
        })

    def get(self, request, **kwargs):

        return render(
            request,
            'richtexts/upload_form.html',
            {}
        )
