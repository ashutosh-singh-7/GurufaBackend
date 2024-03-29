from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import http, timezone
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTP
from .serializers import userInfoSerializer
import random
from twilio.rest import Client
from .validators import password_validator
import requests

def sendHtmlEmail(subject,  recipient_list, email_template_name, email_template_context):
    html_message = render_to_string(email_template_name, email_template_context)
    send_mail(subject=subject, message='', from_email=settings.DEFAULT_FROM_EMAIL,recipient_list=recipient_list, html_message=html_message)

def send_verification_email(request, user):
    # Generate the verification link with expiration time
    token = default_token_generator.make_token(user)
    uid = http.urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    verification_link = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
    expiration_time = timezone.now() + timezone.timedelta(days=2)  # Add 2 days to current time
    verification_link_with_expiry = f'{verification_link}?expires={expiration_time.timestamp()}'
    # Build the email subject and content
    subject = 'Verify your email address'
    context = {
        'first_name': user.first_name,
        'email': user.email,
        'verification_link': f'https://{domain}{verification_link_with_expiry}', 
    }
    # Send the email
    sendHtmlEmail(subject=subject, recipient_list=[user.email], email_template_name='verify_email.html', email_template_context=context)


def verify_email(request, uidb64, token):
    try:
         uid = force_str(http.urlsafe_base64_decode(uidb64))
         user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
         user = None
    if user is not None and default_token_generator.check_token(user, token): 
        expiration_timestamp = float(request.GET.get('expires', 0))
        if timezone.now().timestamp() <= expiration_timestamp:
             user.is_email_verified = True  # Update the user's status or perform any other desired action
             user.save()
             return redirect('https://gurufa.netlify.app/')
        else:
             return HttpResponse('Verification link has expired.')
    else:
         return redirect('https://gurufa.netlify.app/')




"""MSG_91"""
# def sendOtpSMS(user_phone_number, otp): #MSG91
#     user_phone_number='+918210485920' # Remove this line in production

#     url = "https://control.msg91.com/api/v5/flow/"
#     msg91_authkey = settings.MSG91_AUTHKEY
#     template_id = settings.MSG91_TEMPLATE_ID

#     payload = {
#         "template_id": template_id,
#         "short_url": "1", #1 (On) or 0 (Off)
#         "recipients": [
#             {
#                 "mobiles": user_phone_number, #"919XXXXXXXXX"
#                 "OTP": otp,
#             }
#         ]
#     }
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "authkey": msg91_authkey
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     print(response.text)

def sendOtpSMS(user_phone_number, otp):
    user_phone_number='+918210485920' # Remove this line in production
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                        body=f"Your OTP phone verification from Gurufa Kids is {otp}",
                        from_=str(settings.TWILIO_PHONE_NUMBER),
                        to=str(user_phone_number),
                    )
    print(message.sid)


def generate_otp(user):
    otp_code = str(random.randint(1000, 9999))
    OTP.objects.create(user=user, otp_code=otp_code)
    return otp_code


def sendOTP(user):
    try:
        otp = generate_otp(user=user)
        sendOtpSMS(user_phone_number=user.phone_number,otp=otp)
        return otp
    except Exception as error:
        raise error

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def resendOtp(request):
    try:
        sendOTP(request.user)
        return Response({'sent': True}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'sent': False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_phone(request):
    user = request.user
    otp_code = request.data.get('OTP')
    try:
        otp_instance = OTP.objects.get(user=user, otp_code=otp_code)
        user.is_phone_verified = True
        user.save()
        otp_instance.delete()
        return Response({'message': 'OTP verification successful.', 'user_data': userInfoSerializer(user).data}, status=status.HTTP_200_OK)
    except OTP.DoesNotExist:
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


def send_password_reset_email(request, user):
    # Generate the verification link
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    reset_link = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})

    # Build the email subject and content
    subject = 'Reset Your Gurufa Password'
    context = {
        'first_name': user.first_name,
        'email': user.email,
        'reset_link': f'https://{domain}{reset_link}',
    }

    # Send the email
    sendHtmlEmail(subject=subject, recipient_list=[user.email], email_template_name='reset_password_email.html', email_template_context=context)

def resetKeyView(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password') 
            validateKay =  password_validator(password)
            if validateKay[0] :
                user.set_password(password)
                user.save()
                data = {
                    'success': True,
                }
                # Send Confirmation Email
                subject = 'Password Changed Successfully'
                context = {
                    'first_name': user.first_name,
                    'email': user.email,
                }

                sendHtmlEmail(subject=subject, recipient_list=[user.email], email_template_name='password_changed_email.html', email_template_context=context)
                return JsonResponse(data=data)
            else:
                data = {
                    'success': False,
                    'error': validateKay[1]
                }
                return JsonResponse(data=data)

        context = {
            'first_name': user.first_name
        }
        return render(request=request, template_name='reset_password.html', context=context)
        
    else:
        raise Http404()
        # return redirect('http://localhost:5173/')
        # return HttpResponse('email_verification_failed')  # Redirect to a failure page