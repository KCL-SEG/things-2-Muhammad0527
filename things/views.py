from django.shortcuts import render
from .forms import ThingForm
def home(request):
    return render(request, 'home.html')

def things_form(request):
    form = ThingForm()
    return render(request, 'thing.html', {'form': form})
