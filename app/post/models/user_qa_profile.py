from django.db import models
from django.contrib.auth import get_user_model
from common.models import BaseModel

User = get_user_model()


class UserQAProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qa_profiles')
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email} - {self.question.question_text}"

    def get_related_post(self):
        return self.question.post
