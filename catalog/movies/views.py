from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'name': 'Mehmet Faruk Akbulut'
    }
    return render(request, 'movies/list.html', context)

def detail(request):
    return render(request, 'movies/detail.html')
def search(request):
    return render(request, 'movies/search.html')