# core/serializers.py

from rest_framework import serializers
from .models import Sport


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = ("id", "name", "definition", "image", "author", "realized")