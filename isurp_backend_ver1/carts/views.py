from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import CartModel

# Create your views here.


class get_cart(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        uid = request.query_params.get('uid')

        try:
            cart_query = CartModel.objects.get(uid = uid)
            data = {
                    'cartContents': cart_query.cartContents,
                    'cartNonce': cart_query.cartNonce,
                    'cartTotals': cart_query.cartTotals,
                    'currency': cart_query.currency,
                    'cartFees': cart_query.cartFees,
                }
        except:
            data = {'status':'No user'}
        
        response = json.dumps(data)
        return Response(response, status= 200)


class remove_item(APIView):

    def post(self, request):
        uid = request.query_params.get('uid')

        key = request.query_params.get('key')

        try:
            cart_query = CartModel.objects.get(uid = uid)
            for i in range(len(cart_query.cartContents)):
                if cart_query.cartContents[i].key == key:
                    
                    'cartNonce': cart_query.cartNonce,
                    'cartTotals': cart_query.cartTotals,
                    'currency': cart_query.currency,
                    'cartFees': cart_query.cartFees,
            data 
        except:
            data = {'status':'No user'}

