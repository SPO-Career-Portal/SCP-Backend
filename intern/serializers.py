from rest_framework import serializers
from .models import Intern


class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = (
            "intern_name",
            "company",
            "duration",
            "role",
            "description",
            "deadline",
            "intern_start_month",
            "intern_end_month",
        )
