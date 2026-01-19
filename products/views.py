from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def detail(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request, 'detail.html',{'product':product})


def create(request):
    if request.method=='POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        Product.objects.create(
            name=name,
            category=category,
            price=price,
            quantity=quantity,

        )
        return redirect('index')
    return render(request, 'create_product.html')


def update_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')

        product.save()
        return redirect('index')

    return render(request, 'update_product.html', {'product': product})


def delete_product(request, product_id):

    product = Product.objects.get( id=product_id)
    product.delete()

    return redirect('index')