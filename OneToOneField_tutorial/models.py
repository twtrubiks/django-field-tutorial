from django.conf import settings
from django.db import models


# OneToOneField_tutorial

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'