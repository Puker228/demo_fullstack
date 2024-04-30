from .models import Demo
from rest_framework import serializers


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'
