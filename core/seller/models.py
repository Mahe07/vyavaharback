from django.db import models
import uuid 
from django.utils import timezone
from django_base64field.fields import Base64Field

# Create your models here.

Seller_Status = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Draft','Draft'),    
    ('Declined','Declined'),
    )
Seller_Type = (
    ('Distributor','Distributor'),
    ('Manufacturer','Manufacturer'),
    ('Reseller','Reseller'),    
    )

Cluster = (
    ('South','South'),
    ('North','North'),
    ('East','East'),    
    ('West','West'),    
    )
bank_verification = (
    ('Pending','pending'),
    ('Approved','Approved'),   
    )


   
class Seller(models.Model):
    seller_status = models.CharField(choices=Seller_Status,max_length=100,default="Pending",null=True)
    org_id = models.UUIDField(default = uuid.uuid4,null=True)
    owner_name = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=200,null=True)
    mobile_number = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=100,null=True)
    pin_code = models.CharField(max_length=6,null=True)
    cancelled_cheque = Base64Field(max_length=999999999999)
    gst_certificate = Base64Field(max_length=999999999999,null=True)
    drug_license = Base64Field(max_length=999999999999,null=True,blank=True)
    other_license = Base64Field(max_length=999999999999,null=True,blank=True)
    trade_license = Base64Field(max_length=999999999999,null=True,blank=True)
    aadhaar_card = Base64Field(max_length=999999999999,null=True)
    pan_card = Base64Field(max_length=999999999999,null=True)
    description = models.TextField(null=True,blank=True)
    seller_type = models.CharField(choices=Seller_Type,max_length=100,null=True,blank=True)
    time_slot = models.CharField(max_length=100,null=True,blank=True)
    language = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    cluster = models.CharField(choices=Cluster,max_length=100,null=True,blank=True)
    gst_number = models.CharField(max_length=100,null=True,blank=True)
    category = models.IntegerField(null=True, blank=True)
    seller_logo = Base64Field(max_length=999999999999,null=True,blank=True)
    seller_story = models.CharField(max_length=300,null=True,blank=True)
    verified_by = models.CharField(max_length=100,null=True,blank=True)
    approved_by = models.CharField(max_length=100,null=True,blank=True)
    status_description = models.TextField(null=True,blank=True)
    prepaid_commision = models.FloatField(null=True,blank=True)
    postpaid_commision = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"


class Bank_details(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    bank_verification = models.CharField(choices=bank_verification,max_length=100,default="Pending",null=True)
    acct_no = models.CharField(max_length=100,null=True,blank=True)
    bank_name = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    branch = models.CharField(max_length=100,null=True,blank=True)
    ifsc = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.bank_name


class Ldc_details(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    certificate_no= models.CharField(max_length=100,blank=True,null=True)
    tax_rate = models.IntegerField()
    ifsc = models.CharField(max_length=100,null=True,blank=True)
    document = Base64Field(max_length=999999999999,null=True)
    validity_from = models.DateField(null=True)
    validity_to = models.DateField(null=True)
    amount=models.FloatField(null=True)
    def __str__(self):
        return self.certificate_no

class seller_employee(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,null=True)
    name= models.CharField(max_length=100,null=True,blank=True)
    role= models.CharField(max_length=100,null=True,blank=True)
    mobile_number = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

