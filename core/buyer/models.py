from django.db import models
from django_base64field.fields import Base64Field
import uuid 

Buyer_Status = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),
    ('Draft', 'Draft'),    
    )
Buyer_Type = (
    ('Retailer', 'Retailer'),
    ('Commision_Agent', 'Commision_Agent'), 
    )
Cluster = (
    ('South','South'),
    ('North','North'),
    ('East','East'),    
    ('West','West'),    
    )
# Create your models here.

class Buyer(models.Model):
    org_id = models.UUIDField(default = uuid.uuid4,null=True)
    buyer_status = models.CharField(choices=Buyer_Status,max_length=100,default="Pending",null=True,blank=True)
    owner_name = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=200,null=True)
    pin_code = models.CharField(max_length=6,null=True)
    mobile_number = models.CharField(max_length=12,null=True)
    email = models.CharField(max_length=100,null=True)
    gst_certificate = Base64Field(max_length=999999999999,null=True,blank=True)
    fssai_license = Base64Field(max_length=999999999999,null=True,blank=True)
    udhyaam_certificate = Base64Field(max_length=999999999999, blank=True, null=True)
    drug_license = Base64Field(max_length=999999999999, blank=True, null=True)
    trade_license = Base64Field(max_length=999999999999, blank=True, null=True)
    scale_licence = Base64Field(max_length=999999999999, blank=True, null=True)
    address= models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    pan_number = models.CharField(max_length=10,null=True,blank=True)
    gst_number = models.CharField(max_length=100,null=True,blank=True)
    cluster = models.CharField(choices=Cluster,max_length=100,null=True,blank=True)
    district= models.CharField(max_length=100,null=True,blank=True)
    verified_by = models.CharField(max_length=100,null=True,blank=True)
    approved_by = models.CharField(max_length=100,null=True,blank=True)
    status_description = models.TextField(null=True,blank=True)
    buyer_type = models.CharField(choices=Buyer_Type,max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyer"
