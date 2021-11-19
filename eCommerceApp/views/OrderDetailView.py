from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from eCommerceApp.serializers.order_detailSerializer import OrderDetailSerializar
from eCommerceApp.models.order_detail import OrderDetail


@api_view(['GET', 'POST'])
def order_detail_view(request, user=None):
    if request.method == 'GET':
        order_detail = OrderDetail.objects.filter(id_user=user)
        order_detail_serializer = OrderDetailSerializar(order_detail, many=True)
        return Response(order_detail_serializer.data)

    elif request.method == 'POST':
        if request.data["ord_detail"] == 0:
            order_detail = OrderDetail.objects.last()
            order_detail_serializer = OrderDetailSerializar(order_detail)
            if order_detail_serializer.data["ord_detail"] is not None:
                num_ord_detail = order_detail_serializer.data["ord_detail"] + 1
            else:
                num_ord_detail = 1
            request.data["ord_detail"] = num_ord_detail
        request.data["id_user"] = user
        order_detail_serializer = OrderDetailSerializar(data=request.data)
        order_detail_serializer.is_valid(raise_exception=True)
        order_detail_serializer.save()
        return Response({'estado': 'Detalle Orden creada', 'num_orden_det': request.data["ord_detail"]},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def order_detail2_view(request, user=None, pk=None):
    if request.method == 'GET':
        order_detail = OrderDetail.objects.filter(ord_detail=pk, id_user=user)
        order_detail_serializer = OrderDetailSerializar(order_detail, many=True)
        return Response(order_detail_serializer.data)

    elif request.method == "DELETE":
        order_detail = OrderDetail.objects.filter(ord_detail=pk, id_user=user)
        order_detail.delete()
        return Response("Eliminado")


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail3_view(request, user=None, pk=None, product=None):
    if request.method == 'GET':
        order_detail = OrderDetail.objects.filter(ord_detail=pk, id_user=user, id_prod=product).first()
        order_detail_serializer = OrderDetailSerializar(order_detail)
        return Response(order_detail_serializer.data)

    elif request.method == "PUT":
        request.data["id_user"] = user
        request.data["ord_detail"] = pk
        request.data["id_prod"] = product
        order_detail = OrderDetail.objects.filter(ord_detail=pk, id_user=user, id_prod=product).first()
        order_detail_serializer = OrderDetailSerializar(order_detail, data=request.data)
        order_detail_serializer.is_valid(raise_exception=True)
        order_detail_serializer.save()
        return Response(order_detail_serializer.data)

    elif request.method == "DELETE":
        order_detail = OrderDetail.objects.filter(ord_detail=pk, id_user=user, id_prod=product).first()
        order_detail.delete()
        return Response("Eliminado")

