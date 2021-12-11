from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from eCommerceApp.serializers.orderSerializer import OrderSerializer
from eCommerceApp.models.order import Order
from datetime import date


@api_view(['GET', 'POST'])
def order_view(request, user=None):

    if request.method == 'GET':
        order = Order.objects.filter(user=user)
        order_serializer = OrderSerializer(order, many=True)
        return Response(order_serializer.data)

    elif request.method == 'POST':
        order = Order.objects.filter(user=user, order_detail=request.data['order_detail'])
        order_ser = OrderSerializer(order, many=True)
        if len(order_ser.data) > 0:
            return Response({'status': 'Error', 'message': 'La orden ya se encuentra creada'},
                            status=status.HTTP_202_ACCEPTED)
        request.data['date'] = date.today()
        request.data["user"] = user
        order_serializer = OrderSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()
        return Response({'status': 'Orden creada', 'message': str(order_serializer.data)},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_order_view(request, user=None, pk=None):
    if request.method == 'GET':
        order = Order.objects.filter(user=user, id=pk).first()
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data)

    elif request.method == "PUT":
        request.data['date'] = date.today()
        request.data["user"] = user
        order = Order.objects.filter(user=user, id=pk).first()
        order_serializer = OrderSerializer(order, data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()
        return Response(order_serializer.data)

    elif request.method == "DELETE":
        order = Order.objects.filter(user=user, id=pk).first()
        order.delete()
        return Response("Eliminado")
