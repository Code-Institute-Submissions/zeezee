from django.shortcuts import render

# Create your views here.

#View to render the bag itself

def view_bag(request):
   
    return render(request, 'bag/bag.html')
