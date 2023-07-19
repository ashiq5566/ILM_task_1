from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    tag = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title