from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from eCommerceApp.serializers.userSerializer import UserSerializer
from eCommerceApp.models.user import User


@api_view(['GET', 'POST'])
def user_view(request, user=None):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
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
        user = User.objects.filter(id_usu=user).first()
        user_serializer = UserSerializer(user, data=request.data)
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
            serializer.validated_data['UserId'] = token_data['user_id']
        except TokenError as e:
            raise InvalidToken(e.args[0])
    return Response(serializer.validated_data, status=status.HTTP_200_OK)
