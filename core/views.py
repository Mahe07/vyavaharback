from .models import *
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth
from.seller.models import *
from.buyer.models import *
from.product.models import *
from.seller.serializers import *
from.buyer.serializers import *
from.product.serializers import *
import random
import datetime
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail

# Admin
@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    loguser = auth.authenticate(username=request.data['username'],password=request.data['password'])
    if loguser is not None:
        LoginOtp.objects.filter(mobile_number=9658343435).delete()
        Email_Otp.objects.filter(email='manassahoocsk@gmail.com').delete()
        mobile_otp = random.randint(100000, 999999)
        email_otp = random.randint(100000, 999999)
        LoginOtp.objects.create(otp=mobile_otp,mobile_number=9658343435,valid_till = datetime.now() + timedelta(minutes=15))
        Email_Otp.objects.create(otp=email_otp,email='manassahoocsk@gmail.com',valid_till =datetime.now() + timedelta(minutes=15))
        message = "Your OTP for Vyavhar login is {}. OTP is valid for 15 minutes only.".format(mobile_otp)
        email_message = "Your OTP for Vyavhar login is {}. OTP is valid for 15 minutes only.".format(email_otp)
        send_mail(
        'Vyavahar Verification',
        email_message,
        'thedeadmancoc@gmail.com',
        ['manassahoocsk@gmail.com'],
        fail_silently=False,
        )
        data = {'username':request.data['username'],'user_id':loguser.pk}
        return Response(data,status=status.HTTP_200_OK)  
    return JsonResponse(data={"message": "Username or Password Incorrect"}, status=403)  

# Admin
@api_view(['POST'])
@permission_classes([AllowAny])
def admin_otp_verify(request):
    loguser = auth.authenticate(username=request.data['username'],password=request.data['password'])
    if loguser is not None:
        if not Email_Otp.objects.filter(email='manassahoocsk@gmail.com').exists():
            return JsonResponse(data={"message": "Email ID Not Found"},status=404)
        if not LoginOtp.objects.filter(mobile_number=9658343435).exists():
            return JsonResponse(data={"message": "Mobile Number Not Found"},status=404)
        email_otp = Email_Otp.objects.get(email='manassahoocsk@gmail.com')
        mobile_otp = LoginOtp.objects.get(mobile_number=9658343435)
        if email_otp.valid_till < datetime.now() or int(email_otp.otp) != int(request.data["email_otp"]):
            return JsonResponse(data={"message": "Incorrect Email OTP"}, status=403)
        if mobile_otp.valid_till < datetime.now() or int(mobile_otp.otp) != int(request.data["mobile_otp"]):
            return JsonResponse(data={"message": "Incorrect Mobile OTP"}, status=403)
        s = SessionStore()
        s['user_id'] = str(loguser.pk)
        s['user_type'] = 'Admin'
        s.save()  
        x = Session.objects.get(pk=s.session_key)
        x.expire_date = datetime.now()+timedelta(days=1)
        x.save()
        return JsonResponse(data={"message": "Verification Successful",'admin_token':s.session_key,'username':loguser.username},status=200)
    return JsonResponse(data={"message": "Username or Password Incorrect"}, status=403)

# Admin
# 22.04.2021
@api_view(['POST'])
@permission_classes([AllowAny])
def admin_logout(request): 
    if Session.objects.filter(pk=request.data["admin_token"]).exists():
        Session.objects.filter(pk=request.data["admin_token"]).delete()
        return JsonResponse(data={"message": "logout successfully"}, status=200)
    return JsonResponse(data={"message": "You are not logged in. Please log in and try again"}, status=403)


# # 22.04.2021
# #  Admin Session Verification and Fetch All Product, Seller and Buyer
# @api_view(['POST'])
# @permission_classes([AllowAny])  
# def admin_fetch_all(request):
#     if Session.objects.filter(pk=request.data['admin_token1']).exists():
#         session1 = Session.objects.get(pk=request.data['admin_token1'])
#         token1 = session1.get_decoded()
#         if datetime.fromisoformat(token1["login_time"]) < datetime.now() or token1["user_type"] != 'Admin':
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#         if Session.objects.filter(pk=request.data['admin_token2']).exists():
#             session2 = Session.objects.get(pk=request.data['admin_token2'])
#             token2 = session2.get_decoded()
#             if datetime.fromisoformat(token2["login_time"]) < datetime.now() or token2["admin_mobile"] != '9658343435':
#                 return Response(status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return HttpResponse(status=404)
#         if Session.objects.filter(pk=request.data['admin_token3']).exists():
#             session3 = Session.objects.get(pk=request.data['admin_token3'])
#             token3 = session3.get_decoded()
#             if datetime.fromisoformat(token3["login_time"]) < datetime.now() or token3["admin_email"] != 'manassahoocsk@gmail.com':
#                 return Response(status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return HttpResponse(status=404)
#         # Fetch All Product, Seller and Buyer
#         seller = Seller.objects.all()
#         seller = SellerSerializer(seller, many=True)
#         buyer = Buyer.objects.all()
#         buyer = BuyerSerializer(buyer, many=True)
#         product = Product.objects.all()
#         product = ProductSerializer(product, many=True)
#         data = {"seller":seller.data,"buyer":buyer.data,"product":product.data}
#         return Response(data)
#     return HttpResponse(status=404)
