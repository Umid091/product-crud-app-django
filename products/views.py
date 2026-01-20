from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Product
from django.views import View

class ListView(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request, 'index.html', {'products': products})

class DetailView(View):
    def get(self,request,pk):
        product=Product.objects.filter(id=pk).first()
        return render(request, 'detail.html',{'product':product})


class CreateView(View):
    def get(self,request):
        return render(request, 'create_product.html')

    def post(self,request):
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product=Product.objects.create(

            name=name,
            category=category,
            price=price,
            quantity=quantity,
        )
        product.save()
        return redirect('index')


class UpdateView(View):
    def get(self, request, pk):

        product = Product.objects.filter(id=pk).first()
        # Uni HTML-ga context sifatida yuboramiz
        return render(request, 'update_product.html', {'product': product})

    def post(self, request, pk):
        product = Product.objects.filter(id=pk).first()

        if product:
            product.name = request.POST.get('name')
            product.category = request.POST.get('category')
            product.price = request.POST.get('price')
            product.quantity = request.POST.get('quantity')

            product.save()

        return redirect('index')


class DeleteView(View):
    def get(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        product.delete()



    #


# def index(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})
#
# def detail(request,product_id):
#     product=Product.objects.get(id=product_id)
#     return render(request, 'detail.html',{'product':product})
#
#
# def create(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         category = request.POST.get('category')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         Product.objects.create(
#             name=name,
#             category=category,
#             price=price,
#             quantity=quantity,
#
#         )
#         return redirect('index')
#     return render(request, 'create_product.html')
#
#
# def update_product(request, product_id):
#
#     product = Product.objects.get(id=product_id)
#
#     if request.method == "POST":
#         product.name = request.POST.get('name')
#         product.category = request.POST.get('category')
#         product.price = request.POST.get('price')
#         product.quantity = request.POST.get('quantity')
#
#         product.save()
#         return redirect('index')
#
#     return render(request, 'update_product.html', {'product': product})
#
#
# def delete_product(request, product_id):
#
#     product = Product.objects.get( id=product_id)
#     product.delete()
#
#     return redirect('index')