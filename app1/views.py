



from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from .forms import PersonForm
from .models import Person



def person_create(request):
  
    
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()  # Save the person to the database
            return redirect('getquery')  # Redirect to a success page or another view
    else:
        form = PersonForm()

    return render(request, 'app1/create_user.html', {'form': form})

def success(request):
    
    name = Person.objects.last()
      

    return HttpResponse(name)