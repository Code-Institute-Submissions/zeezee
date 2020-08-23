from django.shortcuts import render
from .models import SendBack
from .forms import SendBackForm
from django.contrib import messages


def sendback(request):
    new_sendback = None

    if request.method == 'POST':
        sendback_form = SendBackForm(data=request.POST)
        if sendback_form.is_valid():
            new_sendback = sendback_form.save(commit=False)
            new_sendback.save()
            messages.success(request, 'Request successfully sent')
    else:
        sendback_form = SendBackForm()
    return render(request,
                  'sendback/return.html',
                  {'sendback': sendback,
                   'new_sendback': new_sendback,
                   'sendback_form': sendback_form})
