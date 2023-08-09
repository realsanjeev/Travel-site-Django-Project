from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pics = models.ImageField(upload_to="profile_images", default="blank-profile-photo.jpeg")
    location = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True)

    def __str__(self):
        self.user
