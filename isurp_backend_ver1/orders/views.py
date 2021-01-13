from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Order
import uuid
from datetime import datetime
import razorpay



# Create your views here.
keyId = ''
keySecret = ''


class verify_order(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        order_id = request.data.get('order_id')
        razorpay_payment_id = request.data.get('razorpay_payment_id')
        razorpay_signature = request.data.get('razorpay_signature')

        client = razorpay.Client(auth = (keyId, keySecret))
        params_dict = {
            'order_id': order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }

        client.utility.verify_payment_signature(params_dict)



class return_order(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        uid = request.data.get('uid')

        customer_query = Order.objects.create()
        customer_query.billing.firstName = request.data.get('billing_first_name')
        customer_query.billing.lastName = request.data.get('billing_last_name')
        customer_query.billing.address1 = request.data.get('billing_address_1')
        customer_query.billing.city = request.data.get('billing_city')
        customer_query.billing.postcode = request.data.get('billing_postcode')
        customer_query.billing.country = request.data.get('billing_country')
        customer_query.billing.state = request.data.get('billing_state')
        customer_query.billing.email = request.data.get('billing_email')
        customer_query.billing.phone = request.data.get('billing_phone')

        
