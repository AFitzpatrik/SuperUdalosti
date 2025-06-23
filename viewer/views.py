from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from viewer.models import Event


# Create your views here.
class EventDetailView(DetailView):
    model = Event
    template_name = "viewer/event_detail.html"
    context_object_name = "event"