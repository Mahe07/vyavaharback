from django.db import models
from..seller.models import Seller
from django_base64field.fields import Base64Field
# from..buyer.models import Buyer
import uuid 
from django.conf import settings

# Create your models here.

class Category(models.Model):
    category = models.IntegerField(default=0)
    category_name = models.CharField(max_length=200, null=True)
    category_image = Base64Field(max_length=999999999,null=True)
    def __str__(self):
        return self.category_name

Product_Status = (
    ('Approved','Approved'),
    ('Pending','Pending'),
    ('Draft','Draft'),        
    ('Declined','Declined'),    
    )
Sale_Type = (
    ('Piece','Piece'),
    ('Set','Set'), 
    )

class Product(models.Model):
    product_status = models.CharField(choices=Product_Status,max_length=100,default="Pending",null=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    image_1 = Base64Field(max_length=9999999999999999999999999999,null=True)
    image_2 = Base64Field(max_length=9999999999999999999999999999,null=True)
    image_3 = Base64Field(max_length=9999999999999999999999999999,null=True)
    image_4 = Base64Field(max_length=9999999999999999999999999999,null=True)
    image_5 = Base64Field(max_length=9999999999999999999999999999,null=True)
    image_6 = Base64Field(max_length=9999999999999999999999999999,null=True)
    specification = models.TextField(null=True)
    tittle = models.TextField(null=True)
    colour = models.CharField(max_length=100,null=True)
    brand = models.CharField(max_length=100,null=True)
    manufacturer = models.CharField(max_length=100,null=True,blank=True)
    item_type = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    hsn_code = models.IntegerField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    sale_type = models.CharField(choices=Sale_Type,max_length=100,null=True)
    set_quantity = models.CharField(max_length=100,null=True,blank=True)
    set_contains = models.TextField(null=True,blank=True)
    mrp = models.FloatField(null=True)
    def __str__(self):
        return self.tittle
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product"


class Inventory(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    inventory_status = models.CharField(choices=Product_Status,max_length=100,default="Pending",null=True)
    total_quantity = models.IntegerField(null=True)
    low_stock = models.IntegerField(null=True)
    offline_sell_quantity = models.IntegerField(default=0,null=True)
    online_sell_quantity = models.IntegerField(default=0,null=True)
    out_of_stock = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.product.tittle
    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"


class Pricing(models.Model):
    pricing_status = models.CharField(choices=Product_Status,max_length=100,default="Pending",null=True)
    sku_id = models.TextField(default = uuid.uuid4,null=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    gst_slab = models.FloatField(null=True)
    slab = models.CharField(max_length=100,null=True)
    return_day = models.IntegerField(null=True)
    moq_1_start = models.IntegerField(null=True)
    moq_1_end = models.IntegerField(null=True,blank=True)
    moq_1_price = models.FloatField(null=True,blank=True)
    moq_2_start = models.IntegerField(null=True,blank=True)
    moq_2_end = models.IntegerField(null=True,blank=True)
    moq_2_price = models.FloatField(null=True,blank=True)
    moq_3_start = models.IntegerField(null=True,blank=True)
    moq_3_end = models.IntegerField(null=True,blank=True)
    moq_3_price = models.FloatField(null=True,blank=True)
    moq_4_start = models.IntegerField(null=True,blank=True)
    moq_4_end = models.IntegerField(null=True,blank=True)
    moq_4_price = models.FloatField(null=True,blank=True)
    moq_5_start = models.IntegerField(null=True,blank=True)
    moq_5_price = models.FloatField(null=True,blank=True)
    moq_5_end = models.IntegerField(null=True,blank=True)
    offer_stock = models.BooleanField(default=False,null=True)
    offer_start_date = models.DateField(null=True,blank=True)
    offer_end_date = models.DateField(null=True,blank=True)
    offer_details = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.product.tittle
    class Meta:
        verbose_name = "Pricing"
        verbose_name_plural = "Pricings"


