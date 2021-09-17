from django.contrib import admin
from.models import *
from django.contrib.sessions.backends.db import SessionStore

# Register your models here.
admin.site.register(LoginOtp)
admin.site.register(Email_Otp)
admin.site.register(Pincode)

