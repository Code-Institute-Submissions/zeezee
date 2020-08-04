from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    '''
    If there is product in a bag,
    get it from the session
    If it's empty, display an error message,
    then redirect to products page
    Create an empty order form,
    the HTML part of the checkout,
    the context for it, then render them

    '''
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
    