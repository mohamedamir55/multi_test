from .models import CartItems

def count(request,cart_items=0):
    user=request.user
    if user.is_authenticated :
        items=CartItems.objects.filter(user=user)
        cart_items=items.count()
    return {
        'cart_items':cart_items,
    }
