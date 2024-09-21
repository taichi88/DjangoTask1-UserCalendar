from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import date




def calendar(request):
    current_date = date.today()

    return HttpResponse(f'Today is {current_date}')
