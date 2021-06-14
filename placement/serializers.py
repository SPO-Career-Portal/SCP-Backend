from rest_framework import serializers
from .models import Placement


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = ("key", "placement_name", "company", "role", "description", "deadline")
