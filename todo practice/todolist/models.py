from django.db import models

# Create your models here.
class todo(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()
