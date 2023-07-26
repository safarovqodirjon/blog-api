from django.db import models
from common.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(BaseModel):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    images = models.ManyToManyField('Image', blank=True)
    content = models.TextField()
    date_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
