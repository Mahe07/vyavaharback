from core.buyer.serializers import BuyerSerializer
from rest_framework import serializers
from.models import *
from..product.models import *
from..product.serializers import *
from..seller.serializers import *
from..buyer.serializers import *

class CartSerializer(serializers.ModelSerializer):
    product = ProductBuyerSerializer(many=False, read_only=True)
    buyer = BuyerSerializer(many=False, read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'