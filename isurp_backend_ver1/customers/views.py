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
        uid = request.query_params.get('uid')

        
        



class Create_Object(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self,request):
        


