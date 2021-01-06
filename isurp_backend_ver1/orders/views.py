from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import ReviewModel
import uuid
from datetime import datetime



# Create your views here.


class post_order(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        
