from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    title=models.CharField(max_length=100)

class Multimedias(models.Model):
    picture=models.ImageField()

class Comments(models.Model):
    contenet=models.TextField(max_length=300)
    user=models.ForeignKey(to=User, on_delete=models.CASCADE)
    date=models.DateField()

class Post(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    content=models.TextField(max_length=300)
    added_by=models.ForeignKey(to=User, on_delete=models.CASCADE)
    comments=models.OneToOneField(Comments,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tags)
    multimedias=models.OneToOneField(Multimedias,on_delete=models.CASCADE)
    def __str__(self):
        return self.title




# Create your models here.
