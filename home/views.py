from django.shortcuts import render


# Create your views here.
def index(request):
    '''
    Rendering homepage (index.html)
    '''

    return render(request, 'home/index.html')
