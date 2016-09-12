import uuid

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from . import sanatize_next
from .emails import send_registration, send_reset
from .forms import (ActivateForm, LoginForm, RegisterForm, RequestResetForm,
                    ResetForm)

DEFAULT_AUTH_BACKEND = settings.AUTHENTICATION_BACKENDS[-1]


def login_user(request):
    form = LoginForm(request.POST or None)
    next_action = sanatize_next(request)
    status = None
    if request.method == 'POST':
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return HttpResponseRedirect(sanatize_next(request))
        else:
            status = 400
    return render(request,
                  'euth_users/login.html',
                  {'form': form, 'next_action': next_action},
                  status=status)


def logout_user(request):
    logout(request)
    next_action = request.GET.get('next') or request.POST.get('next')
    if next_action:
        return HttpResponseRedirect(next_action)
    else:
        return render_to_response(
            'euth_users/logout.html',
            context_instance=RequestContext(request))


def register_user(request):
    form = RegisterForm(request.POST or None)
    next_action = sanatize_next(request)
    status = None
    if request.method == 'POST':
        if form.is_valid():
            registration = form.register(request)
            registration.next_action = next_action
            registration.save()
            send_registration(request, registration)
            messages.add_message(request, messages.SUCCESS, _(
                'Registration successfull. Check your email account.'))
            return HttpResponseRedirect(next_action)
        else:
            status = 400
    return render(request,
                  'euth_users/register.html',
                  {'form': form, 'next_action': next_action},
                  status=status)


def activate_user(request, token):
    token = uuid.UUID(token)
    form = ActivateForm(request.POST or None, initial={'token': str(token)})
    status = None
    if request.method == 'POST':
        if form.is_valid():
            user, registration = form.activate(request)
            user.save()
            registration.delete()
            user.backend = DEFAULT_AUTH_BACKEND
            login(request, user)

            return HttpResponseRedirect(registration.next_action)
        else:
            status = 400
    return render(request, 'euth_users/activate.html',
                  {'form': form}, status=status)


def reset_request(request):
    form = RequestResetForm(request.POST or None)
    next_action = sanatize_next(request)
    status = None
    if request.method == 'POST':
        if form.is_valid():
            reset = form.request_reset(request)
            reset.next_action = next_action
            reset.save()
            send_reset(request, reset)
            messages.add_message(request, messages.SUCCESS, _(
                'Reset successfull. Check your email account.'))
            return HttpResponseRedirect(next_action)
        else:
            status = 400
    return render(request, 'euth_users/reset.html',
                  {'form': form, 'next_action': next_action},
                  status=status)


def reset_password(request, token):
    token = uuid.UUID(token)
    form = ResetForm(request.POST or None, initial={'token': str(token)})
    status = None
    if request.method == 'POST':
        if form.is_valid():
            user, reset = form.reset_password(request)
            user.save()
            reset.delete()

            user.backend = DEFAULT_AUTH_BACKEND
            login(request, user)

            return HttpResponseRedirect(reset.next_action)
        else:
            status = 400
    return render(request, 'euth_users/reset_password.html',
                  {'form': form},
                  status=status)