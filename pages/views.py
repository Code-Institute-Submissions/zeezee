from django.shortcuts import render

# Create your views here.

def about(request):
    """ Rendering contact (about.html) """

    return render(request, 'pages/about.html')