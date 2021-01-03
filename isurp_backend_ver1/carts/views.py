from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import CartModel, CartContent
from isurp_backend_ver1.products.models import Product
import uuid

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
            flag = False
            for i in range(len(cart_query.cartContents)):
                if cartContents[i].key == key:
                    index = i
                    flag = True
                    break
            
            if flag:
                cart_query.cartTotals.total = cart_query.cartTotals.total - cartContents[index].quantity*int(cartContents[index].formattedPrice)
                del cartContents[index]
                
            
            cart_query.cartContents = cartContents
            
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
                cart_query.cartTotals.total = (int(qnt) - cartContents[index].quantity) * int(cartContents[index].formattedPrice)
                cartContents[index].quantity = int(qnt)
                
            
            cart_query.cartContents = cartContents
            cart_query.cartFees = cartFees
            cart_query.cartTotals = cartTotals
            
            cart_query.save()
            data = {'status':'deleted'}
            
        except:
            data = {'status':'No user'}

        response = json.dumps(data)
        return Response(response,status=200)


class add_to_cart(APIView):

    def post(self, request):
        uid = request.data.get('uid')

        pid = request.data.get('product_id')
        vid = request.data.get('variation_id')
        pid = int(pid)
        vid = int(vid)
        qnt = request.data.get('quantity')

        try:
            cart_query = CartModel.objects.get(uid = uid)

            key = uuid.uuid4

            cartContents = cart_query.cartContents
            cartTotals = cart_query.cartTotals
            product_query = Product.objects.get(_id = pid)

            

            name = models.CharField(max_length=100, default = DEFAULT_VALUE)
            thumb = models.CharField(max_length=100, default = DEFAULT_VALUE)
            cartContents.append(CartContent())
            cartContents[-1].key = key
            cartContents[-1].productId = pid
            cartContents[-1].variationId = vid
            cartContents[-1].quantity = qnt
            cartContents[-1].formattedPrice = product_query.

            cartTotals
            
            cart_query.cartContents = cartContents
            cart_query.cartTotals = cartTotals

            code = 200
        
        except:
            code = 400
        
        response = json.dumps({})
        return Response(response,status=200)

