from django.shortcuts import render,get_object_or_404,redirect
from store.models import Product
from django.contrib.auth.models import User
from .models import CartItems

def add_cart(request,slug =None):
    user=request.user
    product=get_object_or_404(Product,slug =slug)
    if request.method == 'POST':
        size=request.POST.get('size')
        color=request.POST.get('color')
        quantity=request.POST.get('quantity')

    items=CartItems.objects.filter(user=user,product=product,size=size,color=color).exists()
    if not items:
        items=CartItems.objects.create(user=user,product=product,size=size,color=color,quantity=quantity)
        return redirect ('cart:cart')

    items=CartItems.objects.get(user=user,product=product,color=color,size=size)
    items.quantity=quantity
    items.save()
    return redirect ('cart:cart')










def Cart (request):
    return render (request,'cart/cart.html')