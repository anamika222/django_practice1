from django.urls import path
from . import views  # 👈 Import your views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
