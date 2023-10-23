from django.shortcuts import render
from .forms import ThingsForm
def home(request):
    return render(request, 'home.html')

def things_form(request):
    form = ThingsForm()
    return render(request, 'thing.html', {'form': form})
