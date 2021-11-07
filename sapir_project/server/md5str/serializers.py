from rest_framework import serializers

from .models import Md5str


class Md5strSerializer(serializers.ModelSerializer):
    class Meta:
        model = Md5str
        fields = ['id', 'md5str', 'creation_date']
