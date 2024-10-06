from rest_framework import serializers

from .models import Corepath
from .models import CoreUser
from .models import SubCorePath


class SerializerCore(serializers.ModelSerializer):
    class Meta:
        model = Corepath
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        core = Corepath.objects.create(**validated_data)
        return core
#


class SerializerSubCore(serializers.ModelSerializer):
    class Meta:
        model = SubCorePath
        fields = ('id', 'name', 'description', 'core', 'created_at', 'updated_at', 'deleted_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['core'] = SerializerCore(instance.core.all(), many=True).data  # F821
        return representation  # F821


class SerializerCoreU(serializers.ModelSerializer):
    class Meta:
        model = CoreUser
        fields = ('id', 'user', 'sub_core', 'completed', 'url_repo', 'created_at', 'updated_at')

    def create(self, validated_data):
        coruser = CoreUser.objects.create(**validated_data)
        return coruser

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['core'] = SerializerCore(instance.core.all(), many=True).data  # F821
        representation['subcore'] = SerializerSubCore(instance.subcore.all(), many=True).data  # F821
        return representation  # F821
