from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 50,unique=True)
    product_id = models.AutoField
    product_price = models.IntegerField(default = 0)
    product_desc = models.TextField(max_length = 500,default = "")
    product_img = models.ImageField(upload_to="images",default=product_name)

    
    def __str__(self):
        return self.product_name

class Downloads(models.Model):
    user = models.CharField(max_length = 50)
    product = models.CharField(max_length = 50,default = "")

class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    text = models.TextField()

#added here
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    # Add any other profile fields as needed

    def __str__(self):
        return self.user.username


#till here
# models.py

from django.db import models

class Review(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author  # Or whatever you want to represent the review
