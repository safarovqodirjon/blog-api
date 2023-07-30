from ..models import Question

from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('uuid',
                  'question_text',
                  'option1',
                  'option2',
                  'option3',
                  'option4',
                  "correct_option")
