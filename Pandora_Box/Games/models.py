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
