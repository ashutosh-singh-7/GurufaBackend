import uuid
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.conf import settings
from django.db import transaction
import razorpay
from .models import Purchase
from .serializers import PurchaseSerializer
from course.models import Levels, Plans, Schedule
from user.models import User, Kid   
# Create your views here.



@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def CreatePurchase(request):
    payment_method_chosen = request.data.get('payment_method_chosen')
    course_level_id = request.data.get('course_level_id')
    schedule_id = request.data.get('schedule_id')
    plan_selected_id = request.data.get('plan_selected_id')
    kids_selected_ids = request.data.get('kids_selected_ids')
    purchase_price = request.data.get('purchase_price')

    try:
        user = request.user
    except User.DoesNotExist:
        return Response({'error': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course_level = Levels.objects.get(id=course_level_id)
    except Levels.DoesNotExist:
        return Response({'error': 'Invalid course level ID'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Schedule.DoesNotExist:
        return Response({'error': 'Invalid schedule ID'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        plan_selected = Plans.objects.get(id=plan_selected_id)
    except Plans.DoesNotExist:
        return Response({'error': 'Invalid plan selected ID'}, status=status.HTTP_400_BAD_REQUEST)

    kids_selected = user.my_kids.filter(id__in=kids_selected_ids)

    new_booking_id = course_level.to_course.slug[:3] + str(uuid.uuid4().hex[:7])

    purchase = Purchase.objects.create(
        user=user,
        course_level=course_level,
        schedule=schedule,
        plan_selected=plan_selected,
        purchase_price=purchase_price,
        booking_id= new_booking_id.upper()
    )
    purchase.kids_selected.set(kids_selected)

    """DEMO PLAN SELECTED"""
    if purchase_price == 0 or purchase_price < 1:
        purchase.payment_status = 'PAID'
        purchase.payment_method = 'Free Purchase'
        schedule.seats_occupied = int(schedule.seats_occupied) + kids_selected.count()
        purchase.order_id = "free_purchase_" + str(user.username) + str(uuid.uuid4().hex[:8])
        purchase.payment_id = "Free Purchase"
        purchase.order_signature = "Free Purchase"
        schedule.save()
        """Update the demo_course table for Kids"""
        with transaction.atomic():
            for kid in kids_selected:
                kid.demo_courses.add(course_level.to_course)
        purchase.save()
        data = {}
        data['free'] = True
        data['purchase_data'] = PurchaseSerializer(purchase).data
        return Response(data=data, status=status.HTTP_201_CREATED)


    """RAZORPAY ORDER"""
    if payment_method_chosen == 'Razorpay':
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        DATA = {
            "amount": float(purchase.purchase_price) * 100,
            "currency": "INR",
            "receipt": f"receipt@Razorpay{purchase.id}",
            "notes": {
                "purchase_id": purchase.id,
            }
        }
        try:
            razorpay_order = client.order.create(data=DATA)
            purchase.order_id = razorpay_order['id']
            purchase.save()
            response_data = {
                'message': 'Purchase created successfully',
                'order_created': True, 
                'order': razorpay_order,
                'RAZORPAY_KEY_ID': settings.RAZORPAY_KEY_ID 

            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Some error ocurred.'}, status=status.HTTP_400_BAD_REQUEST)
    
    """CASHFREE"""
    if payment_method_chosen == 'Cashfree':
        url = "https://sandbox.cashfree.com/pg/orders"

        payload = {
            "customer_details": {
                "customer_id": user.email,
                "customer_email": user.email,
                "customer_phone": user.phone_number.national_number
            },
            "order_amount": 10,
            "order_currency": "INR",
            "order_id": "cf" + str(user.username) + str(uuid.uuid4().hex[:8])
        }
        headers = {
            "accept": "application/json",
            "x-client-id": settings.CASHFREE_APP_ID,
            "x-client-secret": settings.CASHFREE_SECRET_KEY,
            "content-type": "application/json"
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            print(response)
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(e)


        response_data = {
                'message': 'Purchase created successfully',
                'order_created': True, 
                'order': "cashfree_purchase",
                'CASHFREE_APP_ID': settings.CASHFREE_APP_ID,
                'cf_response': json.loads(response.text)
            }
        return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def successPurchaseRazorpay(request):
    razorpay_payment_id = request.data.get('razorpay_payment_id')
    razorpay_order_id = request.data.get('razorpay_order_id')
    razorpay_signature = request.data.get('razorpay_signature')
    purchase_id = request.data.get('purchase_id')

    try:
        purchase = Purchase.objects.get(id=purchase_id, user=request.user)
        purchase.payment_id = razorpay_payment_id
        purchase.order_signature = razorpay_signature
        if purchase.order_id == razorpay_order_id:
            purchase.payment_status = 'PAID'
            purchase.payment_method = 'Razorpay'
            purchase.schedule.seats_occupied = int(purchase.schedule.seats_occupied) + purchase.kids_selected.count()
            purchase.schedule.save()
            purchase.save()
            purchase_data = PurchaseSerializer(purchase)
            return Response({"updated": True, 'purchase_data': purchase_data.data},  status=status.HTTP_200_OK)
        else :
            return Response({"updated": False, "message": "Order ID didn't matched"}, status=status.HTTP_400_BAD_REQUEST)

    except Purchase.DoesNotExist:
        return Response({'error': 'Purchase Does Not Exists'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def failedPurchaseRazorpay(request):
    razorpay_payment_id = request.data.get('razorpay_payment_id')
    razorpay_order_id = request.data.get('razorpay_order_id')
    razorpay_signature = request.data.get('razorpay_signature')
    purchase_id = request.data.get('purchase_id')

    try:
        purchase = Purchase.objects.get(id=purchase_id, user=request.user)
        purchase.payment_id = razorpay_payment_id
        purchase.order_signature = razorpay_signature
        if purchase.order_id == razorpay_order_id:
            purchase.payment_status = 'FAILED'
            purchase.payment_method = 'Razorpay'
            purchase.save()
            return Response({"updated": True}, status=status.HTTP_200_OK)
        else :
            return Response({"updated": False, "message": "Order ID didn't matched"}, status=status.HTTP_400_BAD_REQUEST)

    except Purchase.DoesNotExist:
        return Response({'error': 'Purchase Does Not Exists'}, status=status.HTTP_400_BAD_REQUEST)


