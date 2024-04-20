from rest_framework import serializers
from beautify.models import UserModel,ShopModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserModel
        read_only_fields=["id"]
        fields="__all__"

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)
    
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShopModel
        read_only_fields=["id"]
        fields="__all__"