from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogpost_images/', null=True)
    def __str__(self):
        return self.title