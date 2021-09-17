from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.http import HttpResponse, JsonResponse
# from core.buyer.models import Buyer
from.serializers import *
from.models import *
from core.buyer.models import Buyer
# Create your views here.

# Admin ,Seller & Buyer <-- Done -->
@api_view(['POST','GET'])
@permission_classes([AllowAny])
def category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            session = Session.objects.get(pk=request.data['token']['admin_token'])
        except Session.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)
        token = session.get_decoded()
        if token['user_type'] == 'Admin' and session.expire_date > timezone.now():
            if Category.objects.filter(category_name=request.data['category']['category_name']).exists():
                return JsonResponse(data={"message": "Category Already exists"}, status=409)
            serializer = CategorySerializer( data=request.data['category'])
            if serializer.is_valid():
                serializer.save()
                category = Category.objects.all()
                serializer = CategorySerializer(category, many=True)
                return Response(serializer.data)
        return JsonResponse(data={"message": "Session Expired"}, status=403)

@api_view(['POST'])
@permission_classes([AllowAny])
def sku(request):
    try:
        session = Session.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    token = session.get_decoded()
    if token['user_type'] == 'Seller' and session.expire_date > timezone.now():
        if Pricing.objects.filter(sku_id=request.data['sku_id']).exists():
            return JsonResponse(data={"message": "Id already exists"}, status=403)  
        return JsonResponse(data={"message": "Id doesn't exists"}, status=201)  
    return JsonResponse(data={"message": "Session Expired"}, status=403)    
    

@api_view(['POST'])
@permission_classes([AllowAny])
def upload(request):
    try:
        session = Session.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    token = session.get_decoded()
    if token['user_type'] == 'Seller' and session.expire_date > timezone.now():
        if Seller.objects.filter(id=token["seller_id"],seller_status="Approved").exists():
            seller = Seller.objects.get(id=token["seller_id"])
            category = Category.objects.get(id=request.data['pricing']['category'])
            product = Product(seller=seller,image_1=request.data['image']['image_1'],image_2=request.data['image']['image_2'],image_3=request.data['image']['image_3'],image_4=request.data['image']['image_4'],image_5=request.data['image']['image_5'],image_6=request.data['image']['image_6'],
            specification = request.data['product_info']['specification'],tittle=request.data['product_info']['tittle'],colour=request.data['product_info']['colour'],brand=request.data['product_info']['brand'],manufacturer=request.data['product_info']['manufacturer'],item_type=request.data['product_info']['item_type'],description=request.data['product_info']['description'],
            hsn_code=request.data['pricing']['hsn_code'],category=category,sale_type=request.data['pricing']['sale_type'],set_quantity=request.data['pricing']['set_quantity'],set_contains=request.data['pricing']['set_contains'],mrp=request.data['pricing']['mrp'])
            product.save()
            product = Product.objects.get(pk=product.pk)
            Inventory.objects.create(seller=seller,product=product,total_quantity=request.data['inventory']['total_stock'],low_stock=request.data['inventory']['low_stock'])
            Pricing.objects.create(seller=seller,product=product,sku_id=request.data['product_info']['sku_id'],gst_slab=request.data['pricing']['gst_slab'],slab=request.data['pricing']['slab'],return_day=request.data['pricing']['return_day'],
            moq_1_start=request.data['pricing']['moq_1_start'],moq_2_start=request.data['pricing']['moq_2_start'],moq_3_start=request.data['pricing']['moq_3_start'],moq_4_start=request.data['pricing']['moq_4_start'],moq_5_start=request.data['pricing']['moq_5_start'],
            moq_1_end=request.data['pricing']['moq_1_end'],moq_2_end=request.data['pricing']['moq_2_end'],moq_3_end=request.data['pricing']['moq_3_end'],moq_4_end=request.data['pricing']['moq_4_end'],moq_5_end=request.data['pricing']['moq_5_end'],
            moq_1_price=request.data['pricing']['moq_1_price'],moq_2_price=request.data['pricing']['moq_2_price'],moq_3_price=request.data['pricing']['moq_3_price'],moq_4_price=request.data['pricing']['moq_4_price'],moq_5_price=request.data['pricing']['moq_5_price'],
            offer_stock=request.data['inventory']['offer_stock'],offer_start_date=request.data['inventory']['offer_start'],
            offer_end_date=request.data['inventory']['offer_end'],offer_details=request.data['inventory']['offer_details'])
            return JsonResponse(data={"message": "Product Upload Successfully"}, status=201)   
        return JsonResponse(data={"message": "Your Application Is Not Approved"}, status=401)    
    return JsonResponse(data={"message": "Session Expired"}, status=403)    
    

# Seller,Buyer And Admin Product   <-- Done -->
@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):
    try:
        session = Session.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if session.expire_date < timezone.now():
        return Response({"message":"Session expired"},status=403)
    token = session.get_decoded()
    # <-- Buyer Request Start-->
    if token['user_type'] == 'Buyer':
        product_list = Product.objects.filter(product_status="Approved")
        productserializer = ProductBuyerSerializer(product_list, many=True)
        if Buyer.objects.filter(pk=token["buyer_id"], buyer_status="Approved").exists():
            # If Request Buyer Is Approved Buyer
            pricing_list = Pricing.objects.filter(pricing_status="Approved")
            pricingserializer = PricingBuyerSerializer(pricing_list, many=True)
            inventory_list = Inventory.objects.filter(inventory_status="Approved")
            inventoryserializer = InventorySerializer(inventory_list, many=True)
            return Response({"product": productserializer.data,"pricing": pricingserializer.data,"inventory": inventoryserializer.data},status=200)
        return Response({"product": productserializer.data},status=200)
    # <-- Seller Request Start-->
    if token['user_type'] == 'Seller':
        if Seller.objects.filter(pk=token["seller_id"], seller_status="Approved").exists():
            # If Seller Buyer Is Approved Buyer
            product_list = Product.objects.filter(seller=token["seller_id"])
            serializer = ProductSellerSerializer(product_list, many=True)
            return Response({"product": serializer.data})
        return Response({"message":"Seller is not Approved"},status=401)
  
@api_view(['POST'])
@permission_classes([AllowAny])
def seller_product(request):
    seller = Seller.objects.get(mobile_number=request.data['seller_mobile'])
    product = Product.objects.filter(seller_id=seller)
    serializer = ProductBuyerSerializer(product, many=True)
    return Response(serializer.data)



@api_view(['PUT', 'GET'])
@permission_classes([AllowAny])
def product_status(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        product.product_status = request.data['product_status']
        product.save()
        return JsonResponse(data={"message": "Approved"}, status=201)


# 22.04.2021
#  Admin Session Verification and upload Category




@api_view(['POST'])
@permission_classes([AllowAny])
def inventory(request,seller_id):
    if Session.objects.filter(pk=request.data['token']).exists():
        session = Session.objects.get(pk=request.data['token'])
        token = session.get_decoded()
        # if datetime.fromisoformat(token["login_time"]) < datetime.now() or token["user_type"] != 'Seller':
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        temp_inventory = Inventory.objects.filter(seller=seller_id)
        print(temp_inventory)
        inventory = []
        for i in temp_inventory:
            if i.product.product_status == 'Approved':
                inventory.append(i)
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def inventory_update(request):
    if Session.objects.filter(pk=request.data['token']).exists():
        session = Session.objects.get(pk=request.data['token'])
        token = session.get_decoded()
        # if datetime.fromisoformat(token["login_time"]) < datetime.now() or token["user_type"] != 'Seller':
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        if Inventory.objects.filter(seller=token["seller_id"], product=request.data["product_id"]).exists():
            inventory = Inventory.objects.get(
                product=request.data["product_id"])
            quantity = inventory.total_quantity + int(request.data["total_quantity"])
            inventory.total_quantity = quantity
            offline_sell_quantity = inventory.offline_sell_quantity + \
                int(request.data["offline_sell_quantity"])
            inventory.offline_sell_quantity = offline_sell_quantity
            inventory.save()
            return JsonResponse(data={"Success": "Inventory Update Succefully"}, status=201)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([AllowAny])
def single_product(request,product_id):
    try:
        session = Session.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if session.expire_date < timezone.now():
        return Response({"message":"Session expired"},status=403)
    token = session.get_decoded()
    # <-- Buyer Request Start-->
    if token['user_type'] == 'Buyer':
        p=Product.objects.get(id=product_id)
        product_list = Product.objects.filter(product_status="Approved",id=product_id)
        productserializer = ProductBuyerSerializer(product_list, many=True)
        if Buyer.objects.filter(pk=token["buyer_id"], buyer_status="Approved").exists():
            # If Request Buyer Is Approved Buyer
            pricing_list = Pricing.objects.filter(pricing_status="Approved",product=p)
            pricingserializer = PricingBuyerSerializer(pricing_list, many=True)
            inventory_list = Inventory.objects.filter(inventory_status="Approved",product=p)
            inventoryserializer = InventorySerializer(inventory_list, many=True)
            return Response({"product": productserializer.data,"pricing": pricingserializer.data,"inventory": inventoryserializer.data},status=200)
        return Response({"product": productserializer.data},status=200)

@api_view(['GET'])
@permission_classes([AllowAny])
def approved_productscount(request):
    count=Product.objects.filter(product_status="Approved").count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def products_count(request):
    count=Product.objects.all().count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def pending_productscount(request):
    count=Product.objects.filter(product_status="Pending").count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def draft_productscount(request):
    count=Product.objects.filter(product_status="Draft").count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def declined_productscount(request):
    count=Product.objects.filter(product_status="Declined").count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def approved_products(request):
    p=Product.objects.filter(product_status="Approved")
    serializer = ProductSellerSerializer(p, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def all_products(request):
    p=Product.objects.all()
    serializer = ProductSellerSerializer(p, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def pending_products(request):
    p=Product.objects.filter(product_status="Pending")
    serializer = ProductSellerSerializer(p, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def draft_products(request):
    p=Product.objects.filter(product_status="Draft")
    serializer = ProductSellerSerializer(p, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def declined_products(request):
    p=Product.objects.filter(product_status="Declined")
    serializer = ProductSellerSerializer(p, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
def inventory_count(request):
    count=Inventory.objects.all().count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def lowstock_count(request):
    count=Inventory.objects.filter(low_stock__lte=5).count()
    return JsonResponse(count, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def outofstock_count(request):
    count=Inventory.objects.filter(out_of_stock=True).count()
    return JsonResponse(count, safe=False)