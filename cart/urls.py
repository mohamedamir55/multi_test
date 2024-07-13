from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
    path('cart/',views.Cart,name='cart'),
    path('add_cart/<str:slug>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/,<int:item_id>/',views.remove,name='remove'),
]

