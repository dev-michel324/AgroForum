from django.db import models
from django.template.defaultfilters import slugify

from user.models import User

# Create your models here.

# CHOICES = (
#     ('1', 'fungos'),
#     ('2', 'virus'),
#     ('3', 'plantas'),
#     ('4', 'solo'),
#     ('5', 'qualidade da água'),
#     ('6', 'ferramentas'),
# )

class Categorys(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Categorys, related_name='post', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static/image_post', blank=True)
    added = models.DateField(auto_now_add=True, blank=True, null=True)
    update = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    added = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.post


