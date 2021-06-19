from rest_framework import serializers
from intern.models import Intern
from placement.models import Placement
from user.models import User
from django.db.migrations.serializer import BaseSerializer
from django.db.migrations.writer import MigrationWriter
from django.core import serializers
from PlacementSerializer import *
from InternSerializer import *
from UserSerializer import *



class RegistrationSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=True)
    isIntern=InternSerializer(many=True)
    isPlacement=PlacementSerializer(many=True)
    # user = serializers.serialize("json", User.objects.all())
    # isPlacement=serializers.serialize("json", Placement.objects.all())
    # isIntern=serializers.serialize("json", Intern.objects.all())
    class Meta:
        model: Registration
        field= ("user","isIntern","isPlacement",)
        depth=1


class GetRegistration(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('user','isIntern','isPlacement',)