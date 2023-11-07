from django.db import models
from django.conf import settings
from django.utils import timezone

class Board(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

class Topic(models.Model):
    subject = models.CharField(max_length=128)

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title