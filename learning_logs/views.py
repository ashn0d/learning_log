from django.shortcuts import render

def index(request):
    """ The home page for learning logs """

    return render(request, 'index.html')