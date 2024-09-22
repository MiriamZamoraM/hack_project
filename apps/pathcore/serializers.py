from rest_framework import serializers

from .models import Corepath
from .models import CoreUser


class SerializerCore(serializers.ModelSerializer):
    class Meta:
        model = Corepath
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        core = Corepath.objects.create(**validated_data)
        return core
#


class SerializerCoreU(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields = ('id', 'user', 'core', 'completed', 'url_repo')

    def create(self, validated_data):
        coruser = CoreUser.objects.create(**validated_data)
        return coruser
