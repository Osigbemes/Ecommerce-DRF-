from itertools import product
from math import prod
from django.contrib import admin
from .models import User, Product, Order, OrderItem, ShippingAddress

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
