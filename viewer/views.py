from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from viewer.models import Event


# Create your views here.
class EventDetailView(DetailView):
    model = Event
    template_name = "viewer/event_detail.html"
    context_object_name = "event"


class HomepageView(ListView):
    model = Event
    template_name = 'viewer/homepage.html'
    context_object_name = 'events'
    ordering = ['start_date']


class EventListView(ListView):
    model = Event
    template_name = "viewer/event_list.html"
    context_object_name = "events"
    ordering = ["start_date"]