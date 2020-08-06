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
        'stripe_public_key': 'pk_test_51Gwsq1KYUvlFY5urDmgP5IKzwOY7gLJbNHgZqYWm4HChIWm9hjJVRCbxi5rjKFiYFsnhXCs49ePQTRQUsBoYF7x400Rx6HopVH',
        'client_secret': 'test secret',
    }

    return render(request, template, context)
    