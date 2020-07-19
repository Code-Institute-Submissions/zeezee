from django.shortcuts import render

# Create your views here.

def about(request):
    """ Rendering about (about.html) """

    return render(request, 'pages/about.html')