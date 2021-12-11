from django.contrib import admin
from .models.order import Order
from .models.order_detail import OrderDetail

admin.register(Order)
admin.register(OrderDetail)
