
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
