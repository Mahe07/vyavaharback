from core.order.models import myorder
from django.contrib import admin
from.models import *

# Register your models here.
admin.site.register(myorder)
admin.site.register(transaction_details)

