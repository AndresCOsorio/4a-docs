from django.contrib import admin
from .models.user import User
from .models.order import Order
from .models.order_detail import OrderDetail

admin.register(User)
admin.register(Order)
admin.register(OrderDetail)
