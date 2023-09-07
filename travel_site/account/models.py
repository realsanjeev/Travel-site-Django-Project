from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(
        upload_to="profile_images",
        default="blank-profile-photo.jpeg")
    location = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return self.user
