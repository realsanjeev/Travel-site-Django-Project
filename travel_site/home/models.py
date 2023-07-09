from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=False)
    message = models.TextField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
#scrollTo=jj4lDE-8RYU4

# aaa Letters, digits and @/