from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.dele
        
        @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image  
    
      
 class Location(models.Model): 
    name = models.CharField(max_length=60)   

    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def __str__(self):
        return self.name 