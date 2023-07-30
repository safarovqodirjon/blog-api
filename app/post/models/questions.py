from common.models import BaseModel
from django.db import models


class Question(BaseModel):
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.PositiveSmallIntegerField(
        choices=((1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')))

    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.question_text
