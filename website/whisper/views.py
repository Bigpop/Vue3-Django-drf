from rest_framework.permissions import IsAdminUser
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View

from .models import Whisper

from website.settings import BASE_DIR
import json

class WhisperList(ListView):
    model = Whisper
    paginate_by = 10
    template_name = 'whisper/whisper_list.html'
    context_object_name = 'whispers'

    def get_queryset(self):
        return Whisper.objects.order_by('-c_time')


def whisper_list(request):
    query_set = Whisper.objects.order_by('-c_time').values()
    query_set = [item for item in query_set]
    query_set = json.dumps(query_set, default=str)

    return HttpResponse(query_set, content_type='application/json')


