from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm, ContactAdmin



# Create your views here.


def about(request, *args, **kwargs):
    return render(request, "pages/about.html", {"page": "about"})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail
                (subject, message, from_email, ['andrekrisztina5@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pages/contact.html", {'page': contact})


def success(request):
    return HttpResponse('Success! Thank you for your message.')
