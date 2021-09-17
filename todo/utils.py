from django.utils import timezone
from django.utils.timezone import timedelta

def next_day():
    return timezone.now() + timedelta(1)