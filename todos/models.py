from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.title
