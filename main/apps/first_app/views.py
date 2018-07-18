from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request,'first_app/index.html',context)

def checkoutdone(request):
    return render(request,'first_app/checkoutdone.html')

def addproduct(request):
    return render(request,'first_app/addproducts.html')

def addprocess(request):
    Product.objects.create(name=request.POST['procuct_name'],price=request.POST['procuct_price'])
    return redirect('/')

def processbuy(request):
    product = Product.objects.get(id=request.POST['product_id'])
    price = product.price
    name = product.name
    quantity = int(request.POST['product_quantity'])
    print(type(quantity))
    final_price = price * quantity
    request.session['final_price'] = final_price
    
    if 'total_price' in request.session:
        request.session['total_price'] += final_price
    else:
        request.session['total_price'] = final_price
    
    if 'number_of_items' in request.session:
        request.session['number_of_items'] += 1
    else:
        request.session['number_of_items'] = 1

    return redirect('/checkout')