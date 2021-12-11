from rest_framework import serializers
from eCommerceApp.models.order_detail import OrderDetail


class OrderDetailSerializar(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'ord_detail', 'amount_prod', 'id_prod', 'id_user']
        read_only_fields = ('created', 'update')

    def create(self, validated_data):
        order_detail_instance = OrderDetail.objects.create(**validated_data)
        return order_detail_instance
