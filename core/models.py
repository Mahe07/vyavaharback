from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Pincode(models.Model):
    pin_code = models.CharField(max_length=100)


class LoginOtp(models.Model):
    mobile_number = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    valid_till = models.DateTimeField(null=True)

    def __str__(self):
        return self.mobile_number
    class Meta:
        verbose_name = "LoginOtp"
        verbose_name_plural = "LoginOtps"

class Email_Otp(models.Model):
    email = models.CharField(max_length=200)
    otp = models.CharField(max_length=6)
    valid_till = models.DateTimeField(null=True)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "Email_Otp"
        verbose_name_plural = "Email_Otps"