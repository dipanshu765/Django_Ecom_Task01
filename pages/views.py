from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def index(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    products = Product.objects.filter(
        Q(description__icontains=q) |
        Q(name__icontains=q) |
        Q(brand__icontains=q)
    )

    context = {
        'products': products,
    }
    return render(request, 'pages/index.html', context)


def product_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product
    }
    return render(request, 'pages/product_page.html', context)


@login_required(login_url='account:login')
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user != product.host:
        return HttpResponse('You are not allowed to do this!!!')

    if request.method == 'POST':
        product.delete()
        return redirect('pages:index')
    return render(request, 'pages/delete_product.html', {'obj': product})


@login_required(login_url='account:login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():

            product = form.save(commit=False)
            product.host = request.user
            product.save()
            return redirect('pages:index')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/add_product.html', context)


@login_required(login_url='account:login')
def updateProduct(request, product_id):
    instance = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pages:index')
    else:
        form = ProductForm(instance=instance)
    context = {'form': form}
    return render(request, 'pages/add_product.html', context)
