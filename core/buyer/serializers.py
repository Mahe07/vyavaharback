from django.contrib.auth.models import User, Group
from rest_framework import serializers
from.models import *


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'