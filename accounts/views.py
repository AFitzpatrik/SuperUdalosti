from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import success
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


# Create your views here.
def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))  # Zůstanu na stejné stránce


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        success(self.request, f'Účet pro uživatele {form.instance.username} byl úspěšně vytvořen!')
        return response
