from rest_framework import serializers
from .models import Intern


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = (
            "key",
            "intern_name",
            "company",
            "role",
            "description",
            "deadline",
        )
