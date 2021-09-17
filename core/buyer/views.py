from .models import *
from ..models import *
from.serializers import *
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import random
from django.http import JsonResponse
import datetime
from..seller.models import *
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
import requests
# Buyer Log In
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    LoginOtp.objects.filter(mobile_number=request.data["mobile_number"]).delete()
    otp = random.randint(100000, 999999)
    mobile = request.data['mobile_number']
    url = "http://www.alertbox.in/pushsms.php?username=beaming&api_password=d286797eqpwu368e9&sender=Vyvahr&to={}&message=%22Dear%20buyer,%0A%0AYour%20OTP%20for%20Vyavahar%20login%20is{}%20.OTP%20valid%20for%203%20minutes.%20Do%20not%20share%20this%20OTP%20with%20anyone.%20%23Do_vyavahar%0A%0ARegards%0ATeam%20Vyavahar.%22&priority=4&e_id=1201162201264147190&t_id=1207162226625566925".format(mobile,otp)
    r = requests.get(url = url)
    LoginOtp.objects.create(otp=otp,mobile_number=request.data["mobile_number"],valid_till=(datetime.now() + timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S"))
    return JsonResponse(data={"message": "OTP sent"},status=201)

# Buyer Log In
@api_view(['POST'])
@permission_classes([AllowAny])
def login_verification(request):
    if LoginOtp.objects.filter(mobile_number=request.data["mobile_number"]).exists():
        send_login_otp = LoginOtp.objects.get(mobile_number=request.data["mobile_number"])
        if (send_login_otp.valid_till) >  datetime.now() and int(send_login_otp.otp) == int(request.data["otp"]):
            if Buyer.objects.filter(mobile_number=request.data["mobile_number"]).exists(): 
                buyer = Buyer.objects.get(mobile_number = request.data["mobile_number"])
                s = SessionStore()
                s['buyer_mobile'] = str(request.data["mobile_number"])
                s['buyer_id'] = str(buyer.pk)
                s['user_type'] = 'Buyer'
                s.create()
                x = Session.objects.get(pk=s.session_key)
                x.expire_date = datetime.now()+timedelta(days=1)
                x.save()
                return JsonResponse(data={"message": "Verification Successful",'token':s.session_key,'username':buyer.company_name},status=200)
            return JsonResponse(data={"message": "Buyer Doesn't Exists","Status":"Deactive"},status=201)
        return JsonResponse(data={"message": "Verification Failed"},status=403)
    return JsonResponse(data={"message": "Verification Failed"},status=403)
# Buyer Register
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = BuyerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        buyer = Buyer.objects.get(mobile_number = request.data["mobile_number"])
        s = SessionStore()
        s['buyer_mobile'] = str(request.data["mobile_number"])
        s['buyer_id'] = str(buyer.pk)
        s['user_type'] = 'Buyer'
        s.create()
        x = Session.objects.get(pk=s.session_key)
        x.expire_date = datetime.now()+timedelta(days=1)
        x.save()
        return JsonResponse(data={"message": "Verification Successful",'token':s.session_key,'username':buyer.company_name},status=201)

# Buyer Logout
@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request): 
    print(request.data["buyer_token"])
    if Session.objects.filter(pk=request.data["buyer_token"]).exists():
        Session.objects.filter(pk=request.data["buyer_token"]).delete()
        return JsonResponse(data={"message": "logout successfully"}, status=200)
    return JsonResponse(data={"message": "You are not logged in. Please log in and try again"}, status=403)

# Buyer List
@api_view(['POST'])
@permission_classes([AllowAny])
def buyer_list(request):
    try:
        session = Session.objects.get(pk=request.data['admin_token'])
    except Session.DoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)
    token = session.get_decoded()
    if token['user_type'] == 'Admin' and session.expire_date > timezone.now():
        buyer = Buyer.objects.all()
        serializer = BuyerSerializer(buyer, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse(data={"message": "Session Expired"}, status=403)


# Buyer Verification
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
            buyer = Buyer.objects.get(pk=request.data['buyer_id'])
        except Buyer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BuyerSerializer(buyer, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            buyer = Buyer.objects.all()
            buyer_serializer = BuyerSerializer(buyer, many=True)
        return JsonResponse(data={"message": "Verfication Success","buyer":buyer_serializer.data}, status=200)
    return JsonResponse(data={"message": "Session Expired"}, status=403)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_businessinfo(request):
    if LoginOtp.objects.filter(mobile_number=request.data["mobile_number"]).exists(): 
        company_name=request.data["company_name"]
        owner_name=request.data["owner_name"]
        email=request.data["email"]
        mobile_number=request.data["mobile_number"]
        pin_code=request.data["pin_code"]
        Buyer.objects.create(owner_name=owner_name,mobile_number=mobile_number,company_name=company_name,email=email,pin_code=pin_code)
        return JsonResponse(data={"message": "business information recorded"},status=201)
    else:
        return JsonResponse(data={"message": "Phone number doen't exists"},status=403)
