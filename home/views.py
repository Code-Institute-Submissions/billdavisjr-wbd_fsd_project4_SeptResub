from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page of the home app (of the site) """
    return render(request, 'home/index.html')
