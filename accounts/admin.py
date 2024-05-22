from django.contrib import admin
from.models import Profil

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display=['user','phone','address1','address2']
    


# Register your models here.
