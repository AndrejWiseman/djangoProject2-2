from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

