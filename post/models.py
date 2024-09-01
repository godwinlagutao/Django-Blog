from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    subheading = models.CharField(max_length=250, null=True, default=1)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='upload/products/', null=True,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def short_content(self):
        return self.content[:200] + '...' if len(self.content)> 200 else self.content # shows only the first 200 characters
