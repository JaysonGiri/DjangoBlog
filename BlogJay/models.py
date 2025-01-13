from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogpost_images/', null=True)
    def __str__(self):
        return self.title