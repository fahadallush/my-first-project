from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login , name='login'),
    path('logout', views.logout, name='logout'),
] + static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
