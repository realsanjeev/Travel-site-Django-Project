from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=128, null=False)
    email = models.EmailField(unique=False, null=False)
    message = models.TextField(max_length=255, null=False)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.publish_date)
    
    