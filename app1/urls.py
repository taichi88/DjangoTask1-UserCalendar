

from django.urls import path
from . import views



urlpatterns = [
    path('person/', views.person_create, name='add_person'),
    path('getquery/', views.success, name='getquery'),
    # Optional success page
    
]