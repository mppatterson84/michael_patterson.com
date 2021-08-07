from django.db import models
from django.utils import timezone
from tasks.utils import next_day


class Task(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        'auth.User', default='auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    due_by = models.DateTimeField(default=next_day)

    def __str__(self):
        return self.title
