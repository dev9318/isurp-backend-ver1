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
        uid = request.data.get('uid')

        key = request.data.get('key')

        try:
            cart_query = CartModel.objects.get(uid = uid)
            cartContents = cart_query.cartContents
            cartFees = cart_query.cartFees
            cartTotals = cart_query.cartTotals
            flag = False
            for i in range(len(cart_query.cartContents)):
                if cartContents[i].key == key:
                    index = i
                    flag = True
                    break
            
            if flag:
                del cartContents[index]
                del cartFees[index]
                del cartTotals[index]
            
            cart_query.cartContents = cartContents
            cart_query.cartFees = cartFees
            cart_query.cartTotals = cartTotals
            
            cart_query.save()
            data = {'status':'deleted'}
            
        except:
            data = {'status':'No user'}

        response = json.dumps(data)
        return Response(response,status=200)


class change_qnt(APIView):

    def post(self, request):
        uid = request.data.get('uid')

        key = request.data.get('key')
        qnt = request.data.get('quantity')

        try:
            cart_query = CartModel.objects.get(uid = uid)
            cartContents = cart_query.cartContents
            cartFees = cart_query.cartFees
            cartTotals = cart_query.cartTotals
            flag = False
            for i in range(len(cart_query.cartContents)):
                if cartContents[i].key == key:
                    index = i
                    flag = True
                    break
            
            if flag:
                cartContents[index].quantity = qnt
                cartFees[index]
                cartTotals[index]
            
            cart_query.cartContents = cartContents
            cart_query.cartFees = cartFees
            cart_query.cartTotals = cartTotals
            
            cart_query.save()
            data = {'status':'deleted'}
            
        except:
            data = {'status':'No user'}

        response = json.dumps(data)
        return Response(response,status=200)