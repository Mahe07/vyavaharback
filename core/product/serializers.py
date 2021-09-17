from rest_framework import serializers
from.models import *    
from..seller.models import *
from..seller.serializers import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSellerSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        

class ProductBuyerSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
class PricingBuyerSerializer(serializers.ModelSerializer):
    product = ProductBuyerSerializer(many=False, read_only=True)
    seller = SellerSerializer(many=False, read_only=True)
    class Meta:
        model = Pricing
        fields = '__all__'
        
class InventorySerializer(serializers.ModelSerializer):
    seller = SellerSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    product = ProductBuyerSerializer(many=False, read_only=True)
    class Meta:
        model = Inventory
        fields = '__all__'
    
