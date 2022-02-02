from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    des=models.TextField(max_length=200)
    images=models.ImageField(upload_to='pro_img',blank=True)

    def __str__(self):
        return self.name

class Signup(models.Model):
    username=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField(default='')
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50,default='')

    def __str__(self):
        return self.username
# class cart(models.Model):
#     category = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name=models.Charfeild(max_length=200)
#     price = models.IntegerField()

#     def __str__(self):
#         return self.name
    
# Create your models here.
class Mycart(models.Model):
    user=models.ForeignKey(Signup, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on= models.DateTimeField(auto_now_add=True,null=True)

class Table(models.Model):
    images=models.ImageField(upload_to='pro_img',blank=True)
    capacity=models.IntegerField(default='')
    status=models.BooleanField(default=False)

class bookingdate(models.Model):
    date=models.DateTimeField()
    def __unicode__(self):
        return self.date