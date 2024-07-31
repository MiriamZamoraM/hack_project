from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "password", "name", "last_name"]

    def create(self, validated_data):
        model = self.Meta.model
        password = validated_data["password"]
        email = validated_data["email"]
        name = validated_data["name"]
        last_name = validated_data["last_name"]

        user = model.objects.create(email=email, name=name, last_name=last_name)
        user.set_password(password)
        user.save()

        return user

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "email": instance.email,
            "name": instance.name,
            "last_name": instance.last_name,
        }


class UserLoginSerializar(serializers.ModelSerializer):
    email = serializers.CharField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
    )

    class Meta:
        model = User
        fields = ("email", "password")
