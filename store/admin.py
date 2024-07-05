from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Tag

# Register your models here. username=admin password=ecommerce

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Tag)