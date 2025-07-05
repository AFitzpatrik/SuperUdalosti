"""
URL configuration for SuperUdalosti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.urls import path, include
from django.views.generic import TemplateView

from accounts.forms import MyAuthForm, MyPasswordChangeForm
from accounts.views import SignUpView, user_logout
from viewer import views
from viewer.views import HomepageView, EventListView, EventFormView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('', HomepageView.as_view(), name='homepage'),
    path('event/create/', EventFormView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    path('accounts/login/', LoginView.as_view(template_name='login_page.html', authentication_form=MyAuthForm),name='login'),
    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/password_change/',PasswordChangeView.as_view(template_name='password_change.html', form_class=MyPasswordChangeForm),name='password-change'),
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='password_reset.html'),name='password-reset'),
    # ostaní defaultní cesty
    path('accounts/',include ('django.contrib.auth.urls')),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('accounts/registration-success/', TemplateView.as_view(template_name='registration_success.html'), name='registration-success'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)