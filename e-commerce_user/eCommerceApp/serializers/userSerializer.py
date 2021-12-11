from rest_framework import serializers
from eCommerceApp.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_usu', 'name', 'lastName', 'document', 'email', 'password', 'cellphone']

    def to_representation(self, obj):
        user = User.objects.get(id_usu=obj.id_usu)
        return {
            "id_usu": user.id_usu,
            "name": user.name,
            "lastName": user.lastName,
            "document": user.document,
            "email": user.email,
            "password": user.password,
            "cellphone": user.cellphone,
            "is_staff": user.is_staff
        }
