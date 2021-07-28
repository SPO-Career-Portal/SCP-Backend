from rest_framework import fields, serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "username",
            "roll",
            "batch",
            "program",
            "department",
            "github",
            "linkedin",
            "mastercv",
            "resume1",
            "resume2",
            "email",
        )
