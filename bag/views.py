from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    '''View to render the bag itself'''
   
    return render(request, 'bag/bag.html')


def add_to_cart(request, item_id):

    '''Add item to the cart, display a success message'''
    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    '''Overwrite the variable with the new version of the bag'''
    return redirect(redirect_url)


def remove_from_cart(request, item_id):

    '''Remove item from the cart'''
    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag')
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return HttpResponse(status=200)
    