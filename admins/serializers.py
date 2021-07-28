from rest_framework import serializers
from intern.models import Intern
from placement.models import Placement


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
            "eligible_batches",
            "eligible_branches",
            "eligible_programmes",
        )


class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = (
            "key",
            "placement_name",
            "company",
            "role",
            "description",
            "deadline",
            "eligible_batches",
            "eligible_branches",
            "eligible_programmes",
        )
