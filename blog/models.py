from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    abstract = models.TextField()
    text = models.TextField()
