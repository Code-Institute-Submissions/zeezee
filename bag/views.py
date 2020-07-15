from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.

#View to render the bag itself

def view_bag(request):
   
    return render(request, 'bag/bag.html')

def add_to_cart(request, item_id):

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
    print(request.session['bag'])
    '''Overwrite the variable with the new version of the bag'''
    return redirect(redirect_url)