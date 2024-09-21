
from django.urls import path
from . import views
from .views import calendar




urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
]
    # Optional success page
    