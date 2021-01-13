from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Order, Address
import uuid
from datetime import datetime
from isurp_backend_ver1.carts.models import CartModel, CartContent
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

        cart_query = CartModel.objects.get(uid = uid)

        client = razorpay.Client(auth = (keyId, keySecret))
        order_amount = cart_query.cartTotals.total
        order_currency = 'INR'
        # order_receipt = 'order_rcptid_11'
        notes = {'uid': uid}

        order_id = client.order.create(amount=order_amount, currency=order_currency, notes=notes)
        

        customer_query = Order.objects.create( 
            billing = Address(
                firstName = request.data.get('billing_first_name'),
                lastName = request.data.get('billing_last_name'),
                address1 = request.data.get('billing_address_1'),
                city = request.data.get('billing_city'),
                postcode = request.data.get('billing_postcode'),
                country = request.data.get('billing_country'),
                state = request.data.get('billing_state'),
                email = request.data.get('billing_email'),
                phone = request.data.get('billing_phone')
                ),
            orderId = order_id,
            cartModel = cart_query,   
        )

        
