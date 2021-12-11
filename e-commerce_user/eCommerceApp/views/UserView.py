from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

from eCommerceApp.serializers.userSerializer import UserSerializer
from eCommerceApp.models.user import User


@api_view(['GET', 'POST'])
def user_view(request):

    if request.method == 'POST':
        make = request.data.copy()
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        make["password"] = make_password(make["password"], some_salt)

        serializer = UserSerializer(data=make)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        auth_data = {
            'email': request.data['email'],
            'password': request.data['password']
        }
        token_serializer = TokenObtainPairSerializer(data=auth_data)
        token_serializer.is_valid(raise_exception=True)
        token_serializer.validated_data["id_user"] = serializer.data["id_usu"]
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def user_detail_view(request, user=None):
    if request.method == 'GET':
        user = User.objects.filter(id_usu=user).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    elif request.method == "PUT":
        user_obj = User.objects.filter(id_usu=user).first()
        serializer = UserSerializer(user_obj)
        if request.data["password"] != serializer.data["password"]:
            some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
            request.data["password"] = make_password(request.data["password"], some_salt)
        user_serializer = UserSerializer(user_obj, data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(user_serializer.data)


@api_view(['POST'])
def verify_token_view(request):
    if request.method == "POST":
        serializer = TokenVerifySerializer(data=request.data)
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        try:
            serializer.is_valid(raise_exception=True)
            token_data = token_backend.decode(request.data['token'], verify=False)
            serializer.validated_data['UserId'] = token_data['user_id_usu']
        except TokenError as e:
            raise InvalidToken(e.args[0])
    return Response(serializer.validated_data, status=status.HTTP_200_OK)
