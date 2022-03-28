from django.contrib import admin
from .models import Product, Offer



class ProductAdmin(admin.ModelAdmin):
	list_display = ('names', 'price', 'stock')

class OffersAdmin(admin.ModelAdmin):
	list_display = ('code', 'description', 'discount')

# admin.site.register(Product)
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OffersAdmin)