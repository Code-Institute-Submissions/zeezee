from django.shortcuts import render

# Create your views here.


def about(request, *args, **kwargs):
    return render(request, "pages/about.html", {"page": "about"})


def contact(request, *args, **kwargs):
    return render(request, "pages/contact.html", {"page": "contact"})
