from django.urls import path
from . import views

urlpatterns = [
   path('report/', views.report_incident, name='report_incident'),
    path('incidents/', views.incident_list, name='incident_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]