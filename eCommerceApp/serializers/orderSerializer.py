from eCommerceApp.models.order import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'date', 'send_type', 'send_price', 'total_charge', 'order_status', 'pay', 'pay_type',
                  'order_detail', 'user']
