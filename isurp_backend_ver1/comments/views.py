from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import ReviewModel
import uuid
from datetime import datetime
from customers.models import Customer


# Create your views here.

class get_review(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self,request):
        pid = request.data.get('product_id')
        
        try:
            review_query = ReviewModel.objects.get(id = pid)
            data = {
                'author':review_query.author,
                'avatar':review_query.avatar,
                'email':review_query.email,
                'rating':review_query.rating,
                'content':review_query.content,
                'date':review_query.date,
            }
            
            review_query.save()

            code = '200'
        except:
            code = '400'

        data = json.dumps({'code':code})        

        return Response(data, status = code)

class post_review(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self,request):
        pid = request.data.get('product_id')
        # email = request.data.get('')
        rating = request.data.get('rating')
        content = request.data.get('content')
        uid = request.data.get('uid')
        author = request.data.get('author')
        
        try:            
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            customer_query = Customer.objects.get(uid = uid)

            review_query = ReviewModel.objects.create(id = pid, author = author, email = customer_query.email, avatar = customer_query.avatarUrl, rating = rating, content = content, date = current_time)  
            review_query.save()

            code = '200'
        except:
            code = '400'

        data = json.dumps({'code':code})        

        return Response(data, status = code)

