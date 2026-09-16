from django.urls import path
from . import views

urlpatterns = [
    path('', views.awareness_page, name='awareness'),
]
