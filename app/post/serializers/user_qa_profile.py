from rest_framework import serializers
from ..models import UserQAProfile, Question
from .questions import QuestionSerializer


class UserQAProfileSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    question_text = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    def get_options(self, obj):
        # Получаем варианты ответов для данного вопроса
        question = obj.question_text
        options = {
            f"option{i}": getattr(question, f"option{i}") for i in range(1, 5)
        }
        return options

    class Meta:
        model = UserQAProfile
        fields = ('user', 'question_text', 'options', 'selected_answer')
        read_only_fields = ('user',)
