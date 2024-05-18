from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from myapp import views


urlpatterns = [
    path('', views.home1, name='home'),
    path('Technicalsupport', views.home, name='Technicalsupport'),
    path('about/', views.about, name='about'),
    path('all_data/', views.details, name="all_data"),
    path('cart/', views.cart, name='cart'),
    path('Offers/', views.Offers, name='Offers'),
    path('ournews/', views.ournews, name='ournews'),
    path('Meals/', views.Meals, name='Meals'),
    path('burgers/', views.burgers, name='burgers'),
    path('potato/', views.potato, name='potato'),
    path('piessection/', views.piessection, name='piessection'),
    path('sweets/', views.sweets, name='sweets'),
    path('Drinks/', views.Drinks, name='Drinks'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path("add_to_cart" , views.add_to_cart, name='add'),
    path('save-cart/', views.save_cart, name='save_cart'),
    path('map/', views.address_autofill, name='map'),    
    path('', include('accounts.urls')),
] + static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
