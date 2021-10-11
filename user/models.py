from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES=(
    ('specialist', 'specialist'),
    ('beginner', 'beginner'),
)

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='static/profile_photos', blank=True)
    type = models.CharField(max_length=10, choices=CHOICES, blank=False)

    def __str__(self):
        return self.email
