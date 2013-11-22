from django.contrib import admin
from models import Categorie, Wishlist

class CategorieAdmin(admin.ModelAdmin):
    model = Categorie

class WishlistAdmin(admin.ModelAdmin):
    model = Wishlist

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Wishlist, WishlistAdmin)
