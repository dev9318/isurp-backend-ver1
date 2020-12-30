from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Customer


# Create your views here.

class get_customer(APIView):

    authentication_classes = []
    permission_classes = []


    def get(self, request):
        uid = request.query_params.get('uid')

        try:
            customer_query = Customer.objects.get(uid = uid)
            data = {
                'id': customer_query._id,
                'email': customer_query.email,
                'firstName': customer_query.firstName,
                'lastName': customer_query.lastName,
                'role': customer_query.role,
                'username': customer_query.username,
                'billing': customer_query.billing,
                'shipping': customer_query.shipping,
                'isPayingCustomer': customer_query.isPayingCustomer,
                'ordersCount': customer_query.ordersCount,
                'totalSpent': customer_query.totalSpent,
                'avatarUrl': customer_query.avatarUrl,
                'guest': customer_query.guest,}
        except:
            data = {'status':'No user'}
        
        response = json.dumps(data)
        return Response(response, status= 200)


class Update_Address(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self,request):
        uid = request.data.get('uid')
        
        try:
            customer_query = Customer.objects.get(uid = uid)
            customer_query.billing.firstName = request.data.get('billing_first_name')
            customer_query.billing.lastName = request.data.get('billing_last_name')
            # customer_query.billing.company = request.data.get('billing_first_name')
            customer_query.billing.address1 = request.data.get('billing_address_1')
            customer_query.billing.city = request.data.get('billing_city')
            customer_query.billing.postcode = request.data.get('billing_postcode')
            customer_query.billing.country = request.data.get('billing_country')
            customer_query.billing.state = request.data.get('billing_state')
            customer_query.billing.email = request.data.get('billing_email')
            customer_query.billing.phone = request.data.get('billing_phone')

            customer_query.save()

            code = '200'
        except:
            code = '500'

        data = json.dumps({'code':code})        

        return Response(data, status = 200)
        


class get_checkoutform(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self,request):

        uid = request.data.get('uid')
        
        try:
            customer_query = Customer.objects.get(uid = uid)
            data = {
            'billing_first_name': customer_query.billing.firstName,
            'billing_last_name': customer_query.billing.lastName,
            'billing_address_1': customer_query.billing.address1,
            'billing_city': customer_query.billing.city,
            'billing_postcode': customer_query.billing.postcode,
            'billing_country': customer_query.billing.country,
            'billing_state': customer_query.billing.state,
            'billing_email': customer_query.billing.email,
            'billing_phone': customer_query.billing.phone
            }
            # customer_query.billing.company = request.data.get('billing_first_name')

            code = 200
        except:
            code = 500

        response = json.dumps(data)        

        return Response(response, status = code)
        
        



class google_signin(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self,request):
        uid = request.data.get('uid')
        name = request.data.get('name')
        email = request.data.get('email')
        # token = request.data.get('token')

        index = len(name) - 1
        for i in range(len(name)):
            if name[i] == '':
                index = i
        first_name = name[0:index+1]
        last_name = name[index+1:]

        Customer.objects.create(
            uid = uid,
            firstName = first_name,
            lastName = last_name,
            email = email,
            ordersCount = 0,
            totalSpent = 0
        )



class facebook_signin(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self,request):
        uid = request.data.get('uid')
        name = request.data.get('name')
        email = request.data.get('email')
        # token = request.data.get('token')



        index = len(name) - 1
        for i in range(len(name)):
            if name[i] == '':
                index = i
        first_name = name[0:index+1]
        last_name = name[index+1:]

        try:
            Customer.objects.create(
                uid = uid,
                firstName = first_name,
                lastName = last_name,
                email = email,
                ordersCount = 0,
                totalSpent = 0,
            )

            code = 200
        except:
            code = 400
        
        data = {'message':'backend response'}
        response = json.dumps(data)        

        return Response(response, status = code)


