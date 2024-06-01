from django.contrib import admin
from.models import Category,Color,Size,ImagePruduct,Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display='name','slug'

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display= 'name','slug'

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display= 'name','slug'

@admin.register(ImagePruduct)
class ImagePruductAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    


    


    

    

