import json
from rest_framework import serializers
from server.common.models import Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["hex_code"]
