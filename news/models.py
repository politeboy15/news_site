from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fname + " " + self.lname
