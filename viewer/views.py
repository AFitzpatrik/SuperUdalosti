from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, FormView, CreateView, UpdateView, DeleteView

from viewer.forms import EventForm
from viewer.models import Event


class OrganizerRequiredMixin:
    """Mixin pro kontrolu, zda je uživatel ve skupině 'organizatori'"""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Musíte být přihlášeni.")
        
        if not request.user.groups.filter(name='organizatori').exists():
            return HttpResponseForbidden("Nemáte oprávnění. Musíte být organizátor.")
        
        return super().dispatch(request, *args, **kwargs)


class EventDetailView(DetailView):
    model = Event
    template_name = "viewer/event_detail.html"
    context_object_name = "event"


class EventListView(ListView):
    model = Event
    template_name = "viewer/event_list.html"
    context_object_name = "events"
    ordering = ["start_date"]


class EventFormView(LoginRequiredMixin, OrganizerRequiredMixin, CreateView): #CREATEVIEW!!!!!! ŠPATNÝ NÁZEV
    #vyžaduje přihlášení, přidává událost, když bude čas přejmenovat na EventCreateView
    #LoginRequiredMixin - pro pouze přihlášené, momentálně nechci, chci aby mohla jen určitá role přidat event
    model = Event
    template_name = "viewer/form.html"
    form_class = EventForm
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        form.instance.owner_of_event = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Formulář není validní")
        return super().form_invalid(form)


class EventUpdateView(LoginRequiredMixin, OrganizerRequiredMixin, UpdateView):
    model = Event
    template_name = "viewer/form.html"
    form_class = EventForm

    def get_success_url(self):
        return reverse("event-detail", kwargs={"pk": self.object.pk})

    def form_invalid(self, form):
        print('Formulář není validní')
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        """Kontrola, zda organizátor může upravovat tuto událost"""
        obj = self.get_object()
        if obj.owner_of_event != request.user:
            return HttpResponseForbidden("Nemáte oprávnění upravit tuto událost.")
        return super().dispatch(request, *args, **kwargs)


class EventDeleteView(LoginRequiredMixin, OrganizerRequiredMixin, DeleteView):
    model = Event
    template_name = "viewer/confirm_delete.html"
    success_url = reverse_lazy('event-list')
    
    def dispatch(self, request, *args, **kwargs):
        """Kontrola, zda organizátor může mazat tuto událost"""
        obj = self.get_object()
        if obj.owner_of_event != request.user:
            return HttpResponseForbidden("Nemáte oprávnění smazat tuto událost.")
        return super().dispatch(request, *args, **kwargs)


class HomepageView(ListView):
    model = Event
    template_name = 'viewer/homepage.html'
    context_object_name = 'events'
    ordering = ['start_date']



