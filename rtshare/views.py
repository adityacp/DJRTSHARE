# Django Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.templatetags.static import static

# Python Imports
import os

# Local Imports
from .models import Share


def index(request):
    return render(request, 'rtshare/index.html')


def create_room(request, room_name=None):
    if room_name:
        new_share = Share.objects.create(name=room_name)
    else:
        new_share = Share.objects.create(name="New Room")
    return redirect(reverse("rtshare:view_room", args=[new_share.uid]))


def view_room(request, room_id):
    share = get_object_or_404(Share, uid=room_id)
    if share.is_locked:
        messages.warning(request, F"The {share.name} is locked")
        return render(request, 'rtshare/index.html')
    static_path = settings.STATIC_ROOT
    path = os.path.join(
        os.getcwd(), static_path, "js", "codemirror", "mode"
    )
    codemirror_files = []
    for mode in os.listdir(path):
        if os.path.isdir(os.path.join(path, mode)):
            codemirror_files.append(
                static("js/codemirror/mode/{0}/{0}.js".format(mode))
                )
    return render(request, 'rtshare/room.html', {
        'share': share, 'codemirror_files': codemirror_files
    })
