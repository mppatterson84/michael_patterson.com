from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    user = models.ForeignKey(
        'auth.User', default='auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    due_by = models.DateTimeField()

    def __str__(self):
        return self.title
