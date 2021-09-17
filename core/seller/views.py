from .models import *
from ..models import *
from..product.models import *
from..product.serializers import *
from.serializers import *
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
import random
import datetime
import requests
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail

# Seller Log In
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    LoginOtp.objects.filter(mobile_number=request.data["mobile"]).delete()
    otp = random.randint(100000, 999999)
    mobile = request.data["mobile"]
    url = "http://www.alertbox.in/pushsms.php?username=beaming&api_password=d286797eqpwu368e9&sender=Vyvahr&to={}&message=%22Dear%20Seller,%0A%0AYour%20OTP%20for%20Vyavahar%20login%20is{}.OTP%20valid%20for%203%20minutes.%20Do%20not%20share%20this%20OTP%20with%20anyone.%20%23Do_vyavahar%0A%0ARegards%0ATeam%20Vyavahar.%22&priority=4&e_id=1201162201264147190&t_id=1207162226643478657".format(mobile,otp)
    r = requests.get(url = url)
    LoginOtp.objects.create(otp=otp,mobile_number=request.data["mobile"],valid_till = datetime.now() + timedelta(minutes=3))
    return JsonResponse(data={"message": "OTP sent"},status=201)

# Seller Log In
@api_view(['POST'])
@permission_classes([AllowAny])
def login_verification(request):
    if LoginOtp.objects.filter(mobile_number=request.data["mobile_number"]).exists():
        send_login_otp = LoginOtp.objects.get(mobile_number=request.data["mobile_number"])
        if send_login_otp.valid_till > datetime.now() and int(send_login_otp.otp) == int(request.data["otp"]):
            if Seller.objects.filter(mobile_number=request.data["mobile_number"]).exists(): 
                seller = Seller.objects.get(mobile_number = request.data["mobile_number"])
                if not Seller.objects.filter(mobile_number=request.data["mobile_number"],seller_status="Approved").exists():
                    return JsonResponse(data={"message": "Your Application is "+ seller.seller_status},status=401)
                s = SessionStore()
                s['seller_mobile'] = str(request.data["mobile_number"])
                s['seller_id'] = str(seller.pk)
                s['user_type'] = 'Seller'
                s.create()
                x = Session.objects.get(pk=s.session_key)
                x.expire_date = datetime.now()+timedelta(days=1)
                x.save()
                return JsonResponse(data={"message": "Verification Successful",'token':s.session_key,'username':seller.company_name,'userid':seller.id},status=200)
            return JsonResponse(data={"message": "Seller Doesn't Exists"},status=201)
        return JsonResponse(data={"message": "Incorrect OTP"},status=403)
    return JsonResponse(data={"message": "Verification Failed"},status=403)

# Seller Register
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = SellerRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

# Seller Register In
@api_view(['POST'])
@permission_classes([AllowAny])
def seller_list(request):
    try:
        session = Session.objects.get(pk=request.data['admin_token'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    token = session.get_decoded()
    if token['user_type'] == 'Admin' and session.expire_date > timezone.now():
        seller = Seller.objects.all()
        seller_serializer = SellerSerializer(seller, many=True)
        category = Category.objects.filter(category=0)
        category_serializer = CategorySerializer(category, many=True)
        return JsonResponse({"seller":seller_serializer.data,"categories":category_serializer.data}, safe=False)
    return JsonResponse(data={"message": "Session Expired"}, status=403)

# Seller Verification
@api_view(['POST'])
@permission_classes([AllowAny])
def document_verficaton(request):
    try:
        session = Session.objects.get(pk=request.data['admin_token'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    token = session.get_decoded()
    if token['user_type'] == 'Admin' and session.expire_date > timezone.now():
        try:
            seller = Seller.objects.get(pk=request.data['seller_id'])
        except Seller.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SellerSerializer(seller, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            seller = Seller.objects.all()
            seller_serializer = SellerSerializer(seller, many=True)
        return JsonResponse(data={"message": "Verfication Success","seller":seller_serializer.data}, status=200)
    return JsonResponse(data={"message": "Session Expired"}, status=403)
@api_view(['GET'])
@permission_classes([AllowAny])
def test_mobile(request):
    otp = random.randint(100000, 999999)
    print(otp)
    mobile = 9090000201
    url = "http://www.alertbox.in/pushsms.php?username=beaming&api_password=d286797eqpwu368e9&sender=Vyvahr&to={}&message=%22Dear%20Seller,%0A%0AYour%20OTP%20for%20Vyavahar%20login%20is{}.OTP%20valid%20for%203%20minutes.%20Do%20not%20share%20this%20OTP%20with%20anyone.%20%23Do_vyavahar%0A%0ARegards%0ATeam%20Vyavahar.%22&priority=4&e_id=1201162201264147190&t_id=1207162226643478657".format(mobile,otp)
    r = requests.get(url = url)
    return JsonResponse(data={"message": "Verfication Success"}, status=200)

@api_view(['GET'])
@permission_classes([AllowAny])
def seller_details(request,userid):
    delivered=Seller.objects.filter(id=userid)
    serializer = SellerSerializer(delivered, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def edit_details(request,userid):
    details=Seller.objects.get(id=userid)
    details.company_name=request.data['company_name']
    details.description=request.data['description']
    details.save()
    return JsonResponse(data={"message": " Successfully updated"}, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def edit_contactdetails(request,userid):
    details=Seller.objects.get(id=userid)
    details.owner_name=request.data['owner_name']
    details.email=request.data['email']
    details.mobile_number=request.data['mobile_number']
    details.time_slot=request.data['time_slot']
    details.language=request.data['language']
    details.save()
    return JsonResponse(data={"message": " Successfully updated"}, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def updatephonenumber(request,userid):
    k=Seller.objects.get(id=userid)
    if request.method=='POST':
        phonenumber=request.data['mobile_number']
        k.mobile_number=phonenumber
        k.save()
    return JsonResponse(data={"message": " Successfully updated"}, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def updateemail(request,userid):
    print(userid)
    k=Seller.objects.get(id=userid)
    email=request.data['email']
    k.email=email
    k.save()
    return JsonResponse(data={"message": " Successfully updated"}, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def seller_bankdetails(request,userid):
    seller=Seller.objects.get(id=userid)
    details=Bank_details.objects.filter(seller=seller).values()
    print(details)
    serializer = BankSerializer(details, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def edit_bankdetails(request,userid,bankid):
    det=Seller.objects.get(id=userid)
    det.company_name=request.data['company_name']
    det.save()
    details=Bank_details.objects.get(id=bankid)
    details.bank_name=request.data['bank_name']
    details.acct_no=request.data['acct_no']
    details.state=request.data['state']
    details.city=request.data['city']
    details.ifsc=request.data['ifsc']
    details.branch=request.data['branch']
    details.save()
    return JsonResponse(data={"message": " Successfully updated"}, safe=False)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_ldcdetails(request,userid):
    det=Seller.objects.get(id=userid)
    certificate_no=request.data['certificate_no']
    tax_rate=request.data['tax_rate']
    document=request.data['document']
    validity_from=request.data['validity_from']
    ifsc=request.data['ifsc']
    amount=request.data['amount']
    validity_to=request.data['validity_to']
    Ldc_details.objects.create(seller=det,certificate_no=certificate_no,ifsc=ifsc,tax_rate=tax_rate,document=document,validity_from=validity_from,validity_to=validity_to,amount=amount)
    return JsonResponse(data={"message": " Successfully added"}, safe=False)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_employee(request,userid):
    det=Seller.objects.get(id=userid)
    name=request.data['name']
    role=request.data['role']
    email=request.data['email']
    mobile_number=request.data['mobile_number']
    seller_employee.objects.create(seller=det,email=email,mobile_number=mobile_number,name=name,role=role)
    return JsonResponse(data={"message": " Successfully added"}, safe=False)

