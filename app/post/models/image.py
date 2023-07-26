from django.db import models
from common.models import BaseModel


class Image(BaseModel):
    title = models.CharField(max_length=255, verbose_name="image-name")
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"Image-{self.title}"
