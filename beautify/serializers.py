from rest_framework import serializers
from beautify.models import UserModel


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserModel
        read_only_fields=["id"]
        fields=["id","email","password"]

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)