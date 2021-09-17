from rest_framework import serializers
from.models import *


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class SellerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['description','owner_name','company_name','pin_code','email','mobile_number','other_license','drug_license','trade_license','gst_certificate','cancelled_cheque','pan_card','aadhaar_card']

class BankSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(many=False, read_only=True)
    class Meta:
        model = Bank_details
        fields = '__all__'


