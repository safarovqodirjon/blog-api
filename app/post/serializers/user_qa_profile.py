from rest_framework import serializers
from ..models import UserQAProfile
from .questions import QuestionSerializer


class UserQAProfileSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = UserQAProfile
        fields = '__all__'
