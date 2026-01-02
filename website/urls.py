from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('amazon_redirect/', views.amazon_redirect, name="amazon_redirect")
]

