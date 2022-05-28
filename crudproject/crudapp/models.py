from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.TextField(max_length=40)
    age=models.TextField()
    address=models.TextField()