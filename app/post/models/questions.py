from common.models import BaseModel
from django.db import models


class Question(BaseModel):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
