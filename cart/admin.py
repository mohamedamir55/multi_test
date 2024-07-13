from django.contrib import admin
from .models import CartItems

@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    list_display='user','product','size','color','quantity','sub_total','total'
    
 