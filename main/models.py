from django.db import models

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
