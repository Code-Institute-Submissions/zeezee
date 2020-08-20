from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    Filter all the category who's name is in the list'
    If the query is empty,
    so the user haven't entered any search term,
    they get an error message
    Pagination with django paginator loading
    8 product/page to improve user experience
    '''
    query = None
    categories = None
    sort = None
    direction = None
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            '''Q variable where the name OR the description
            contain the query, then filter the products'''
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'paginator': paginator,
    }

    return render(request, 'products/products.html', context)


def detail_product(request, product_id):
    '''
    Detailed product view
    '''
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/detail_product.html', context)

@login_required
def edit_product(request, product_id):
    '''
    Login_required decorator added to avoid people
    deleting, editing or adding products with hardtyping the urls
    View for editing products, only allowed for superusers
    '''
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have access to this page.")
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail_product', args=[product.id]))
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def add_new_product(request):
    '''
    Allow the superusers 
    to add a new product with admin
    Render the add_new_product template 
    and the form    
    '''
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have access to this page.")
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_new_product'))
        else:
            messages.error(request, 'Please make sure your form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_new_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    '''
    Delete products
    Only superusers have access to this
    '''
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have acces to this page.")
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'The choosed product was deleted!')
    return redirect(reverse('products'))


