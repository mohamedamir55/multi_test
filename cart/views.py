from django.shortcuts import render,get_object_or_404,redirect
from store.models import Product
from django.contrib.auth.models import User
from .models import CartItems,Coupon
from django.contrib.auth.decorators import login_required

@login_required(login_url='acoounts:login')
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


def remove(request,product_id,item_id):
    user=request.user
    product=Product.objects.get(id=product_id)
    item=CartItems.objects.get(user=user,product=product,id=item_id)
    item.delete()
    return redirect ('cart:cart')






@login_required(login_url='accounts:login')
def Cart (request,discount=0,total=0):
    user=request.user
    items= CartItems.objects.filter(user=user)
    try:
        total=[item.total for item in items][0]
    except:
        pass
    if request.method=='POST':
        code=request.POST.get('code')
        if code :
            coupon=Coupon.objects.filter(code=code,active=True).first()
            if not coupon:
                raise "coupon is Expired"
            ratio=coupon.discount / 100
            discount=total * ratio

    shipping=total*0.10
    grand_total=shipping+(total-discount)
    

    context={
        'items':items,
        'total':total,
        'shipping':shipping,
        'grand_total':grand_total,
        'discount':discount,
    }
    return render (request,'cart/cart.html',context)