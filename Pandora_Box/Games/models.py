from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    product_id = models.AutoField
    product_price = models.IntegerField(default = 0)
    product_desc = models.TextField(max_length = 500,default = "")
    product_img = models.ImageField(upload_to="images",default=product_name)

    
    def __str__(self):
        return self.product_name

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