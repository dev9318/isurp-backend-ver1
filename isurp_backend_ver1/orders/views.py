from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import ReviewModel
import uuid
from datetime import datetime
import razorpay



# Create your views here.
keyId = ''
keySecret = ''


class post_order(APIView):
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


        
