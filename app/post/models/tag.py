from django.db import models
from common.models import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.strip().lower()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
