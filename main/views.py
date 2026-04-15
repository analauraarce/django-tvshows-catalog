from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'dynamic_title': 'Home',
        'dynamic_description': 'Welcome to the TV show catalog built with Django and Bootstrap Green. Explore and enjoy.',
        'dynamic_message': 'Press the Start button to browse the catalog.',
    }
    return render(request, 'main/home.html', context)