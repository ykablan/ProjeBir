from django.urls import path, include
from .views import anaSayfa

urlpatterns = [
    path('', anaSayfa, name='anaSayfa'),
]
