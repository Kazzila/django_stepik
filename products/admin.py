from django.contrib import admin

# Register your models here.
from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = (
        'name', 'description',
        'category', ('price', 'quantity'),
        'stripe_product_price_id', 'image',
    )
    readonly_fields = ('description',)
    search_fields = ('name', 'quantity', 'category')
    ordering = ('price', 'quantity', 'category')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
