from django.db import models
from django.contrib.auth import get_user_model
from common.models import BaseModel

User = get_user_model()


class UserQAProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="qas")
    selected_answer = models.PositiveSmallIntegerField(
        choices=((1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')))

    def __str__(self):
        return f"{self.user} answered question {self.question_text}"
