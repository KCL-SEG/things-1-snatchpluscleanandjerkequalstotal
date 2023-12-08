from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'things/things_page.html', {'title': 'Things'})
