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
                id: json["id"] == null ? 0 : json["id"],
                email: customer_query.email,
                firstName: customer_query.firstName,
                lastName: customer_query.lastName,
                role: customer_query.role,
                username: customer_query.username,
                billing: customer_query.billing.,
                shipping: json["shipping"] == null ? null : Address.fromJson(json["shipping"]),
                isPayingCustomer: json["is_paying_customer"] == null ? null : json["is_paying_customer"],
                ordersCount: json["orders_count"] == null ? null : json["orders_count"],
                totalSpent: json["total_spent"] == null ? null : json["total_spent"],
                avatarUrl: json["avatar_url"] == null ? null : json["avatar_url"],
                guest: json["guest"] == null ? null : json["guest"],}


