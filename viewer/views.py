from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView

from viewer.forms import EventForm
from viewer.models import Event


# Create your views here.
class EventDetailView(DetailView):
    model = Event
    template_name = "viewer/event_detail.html"
    context_object_name = "event"


class EventListView(ListView):
    model = Event
    template_name = "viewer/event_list.html"
    context_object_name = "events"
    ordering = ["start_date"]


class EventFormView(FormView):
    template_name = "viewer/form.html"
    form_class = EventForm
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        Event.objects.create(
            name=cleaned_data['name'],
            description=cleaned_data['description'],
            event_image=cleaned_data.get('event_image'),
            start_date=cleaned_data['start_date'],
            end_date=cleaned_data['end_date'],
            start_time=cleaned_data['start_time'],
            end_time=cleaned_data['end_time'],
            location=cleaned_data['location'],
            owner_of_event=self.request.user  # ← tady je klíčová změna
        )
        return super().form_valid(form)


class HomepageView(ListView):
    model = Event
    template_name = 'viewer/homepage.html'
    context_object_name = 'events'
    ordering = ['start_date']


