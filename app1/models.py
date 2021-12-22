from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    des=models.TextField(max_length=200)
    images=models.ImageField(upload_to='pro_img',blank=True)

    def __str__(self):
        return self.name
    
# class cart(models.Model):
#     category = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name=models.Charfeild(max_length=200)
#     price = models.IntegerField()

#     def __str__(self):
#         return self.name
    
# Create your models here.
