from django.db import models
from datetime import time
# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.cat_name

class MovieCard(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=100)
    links = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    pub_date = models.DateField(default="")
    image = models.ImageField(upload_to="MoviesHub/images" , default="")
    
    def __str__(self):
        return self.name
    

class Request(models.Model):
    rq_id = models.AutoField(primary_key=True)
    request_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.request_name
    
