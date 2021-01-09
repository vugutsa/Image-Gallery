from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_image = models.ImageField(upload_to = '/')
    email = models.EmailField()
    
    
#  class Location(models.Model): 
#     name = models.CharField(max_length=60)   
