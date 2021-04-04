from django.db import models
from django.utils import timezone


class Email(models.Model):
    from_email = models.EmailField(max_length=70, blank=False)
    subject = models.CharField(max_length=70, blank=False)
    message = models.TextField(max_length=700, blank=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.subject
