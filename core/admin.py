from django.contrib import admin
from models import Categorie, Wishlist

class CategorieAdmin(admin.ModelAdmin):
    model = Categorie

class WishlistAdmin(admin.ModelAdmin):
    model = Wishlist