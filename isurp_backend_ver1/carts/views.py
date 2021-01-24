from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import CartModel, CartContent
from products.models import Product
import uuid

# Create your views here.


class get_cart(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        uid = request.query_params.get('uid')

        try:
            cart_query = CartModel.objects.get(uid = uid)
            if cart_query.empty == True:
                data = {'status':'empty'}
            else:
                data = {
                        'cartContents': cart_query.cartContents,
                        'cartNonce': cart_query.cartNonce,
                        'cartTotals': cart_query.cartTotals,
                        'currency': cart_query.currency,
                        'cartFees': cart_query.cartFees,
                    }
            code = 200
        except:
            data = {'status':'No user'}
            code = 400
        
        response = json.dumps(data)
        return Response(response, status= code)


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
                if len(cartContents) == 1:
                    cart_query.empty = True
                else:
                    cart_query.cartTotals.total = cart_query.cartTotals.total - cartContents[index].quantity*int(cartContents[index].formattedPrice)
                    del cartContents[index]
                
            
            cart_query.cartContents = cartContents
            
            cart_query.save()
            if cart_query.empty == True:
                data = {'status':'empty'}
            else:
                data = {
                        'cartContents': cart_query.cartContents,
                        'cartNonce': cart_query.cartNonce,
                        'cartTotals': cart_query.cartTotals,
                        'currency': cart_query.currency,
                        'cartFees': cart_query.cartFees,
                    }
            code = 200
            
        except:
            data = {'status':'No user'}
            code = 400

        response = json.dumps(data)
        return Response(response,status=code)


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
            data = {
                        'cartContents': cart_query.cartContents,
                        'cartNonce': cart_query.cartNonce,
                        'cartTotals': cart_query.cartTotals,
                        'currency': cart_query.currency,
                        'cartFees': cart_query.cartFees,
                    }
            code = 200
            
        except:
            data = {'status':'No user'}
            code = 400

        response = json.dumps(data)
        return Response(response,status=code)


class add_to_cart(APIView):

    def post(self, request):
        uid = request.data.get('uid')

        pid = request.data.get('product_id')
        vid = request.data.get('variation_id')
        pid = int(pid)
        vid = int(vid)
        qnt = request.data.get('quantity')
        qnt = int(qnt)

        try:
            cart_query = CartModel.objects.get(uid = uid)

            key = uuid.uuid4

            cartContents = cart_query.cartContents
            cartTotals = cart_query.cartTotals
            product_query = Product.objects.get(_id = pid)  

            if cart_query.empty == True:
                cart_query.empty = False
                cartContents = []
                cartTotals.subtotal = 0
                cartTotals.total = 0

            name = ''
            index = 0

            for i in range(len(product_query.availableVariations)):
                if product_query.availableVariations.variationId == vid:
                    index = i

            formattedPrice =  product_query.availableVariations[index].formattedPrice
            for i in range(len(product_query.availableVariations[index].option)):
                name = name + product_query.availableVariations[index].option[i].value
            thumb =  product_query.availableVariations[index].image.url

            newItem = CartContent(key = key, productId = pid, variationId = vid, quantity = qnt, formattedPrice = formattedPrice, name = name, thumb = thumb)
            cartContents.append(newItem)

            cartTotals.subtotal = cartTotals.subtotal + qnt*float(formattedPrice)
            cartTotals.total = cartTotals.total + qnt*float(formattedPrice)
            
            cart_query.cartContents = cartContents
            cart_query.cartTotals = cartTotals
            data = {
                        'cartContents': cart_query.cartContents,
                        'cartNonce': cart_query.cartNonce,
                        'cartTotals': cart_query.cartTotals,
                        'currency': cart_query.currency,
                        'cartFees': cart_query.cartFees,
                    }
            code = 200
        
        except:
            data = {'message': 'error occured'}
            code = 400
        
        response = json.dumps(data)
        return Response(response,status=code)


class clear_cart(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        uid = request.query_params.get('uid')

        try:
            cart_query = CartModel.objects.get(uid = uid)
            cart_query.empty = True
            cart_query.save()
            data = {'status':'Cleared'}
            code = 200
        except:
            data = {'status':'No user'}
            code = 400
        
        response = json.dumps(data)
        return Response(response, status= code)