from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from..buyer.models import *
from..product.models import *
from.models import *
from.serializers import *
from django.http import JsonResponse

#Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])   
def add_to_cart(request):
    if 'quantity' in request.data:
        print(request.data)
        buyer = Buyer.objects.get(mobile_number=request.data["mobile_number"])    
        product = Product.objects.get(id=request.data["product_id"])
        x = Cart(product=product,buyer=buyer,quantity=request.data["quantity"])
        x.save()
    else:
        buyer = Buyer.objects.get(mobile_number=request.data["mobile_number"])    
        product = Product.objects.get(id=request.data["product_id"])
        x = Cart(product=product,buyer=buyer)
        x.save()
    return Response( status=status.HTTP_201_CREATED)
@api_view(['GET'])
@permission_classes([AllowAny])   
def cart_list(request,id):
    buyer = Buyer.objects.get(mobile_number=id)    
    cart = Cart.objects.filter(buyer=buyer)
    serializer = CartSerializer(cart, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])   
def cart_delete(request,id):
    Cart.objects.filter(id=id).delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])   
def cart_count(request,id):
    buyer = Buyer.objects.get(mobile_number=id)    
    cart = Cart.objects.filter(buyer=buyer).count()
    return JsonResponse(cart, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])   
def cart_total(request,id):
    buyer = Buyer.objects.get(mobile_number=id)    
    cart = Cart.objects.filter(buyer=buyer)
    total=0
    print(cart)
    for i in cart:
        p = Product.objects.get(id=i.product_id)
        subtotal=i.quantity*p.mrp
        total=total+subtotal
    discount=total*0.05
    discount=int(discount)
    return JsonResponse({'total':total,'discount':discount}, safe=False)
