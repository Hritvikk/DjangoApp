from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class Post(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField()

    def publish(self):
        self.end_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title