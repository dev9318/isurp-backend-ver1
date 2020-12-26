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
                    cartContents: json["cartContents"] == null ? null : new List<CartContent>.from(json["cartContents"].map((x) => CartContent.fromJson(x))),
                    cartNonce: json["cart_nonce"] == null ? null : json["cart_nonce"],
                    cartTotals: json["cart_totals"] == null ? null : CartTotals.fromJson(json["cart_totals"]),
                    points: json["points"] == null ? null : Points.fromJson(json["points"]),
                    purchasePoint: json["purchase_point"] == null ? null : json["purchase_point"],
                    currency: json["currency"] == null ? 'USD' : json["currency"],
                    cartFees: json["cart_fees"] == null ? null : List<CartFee>.from(json["cart_fees"].map((x) => CartFee.fromJson(x))),
                }
        except:
            data = {'status':'No user'}
        
        response = json.dumps(data)
        return Response(response, status= 200)

