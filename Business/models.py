from django.db import models


class Business(models.Model):
    business_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.business_name
    
class Product(models.Model):
    image = models.ImageField()
    product_name = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2)
    sell_price = models.DecimalField(max_digits=6, decimal_places=2)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
       
