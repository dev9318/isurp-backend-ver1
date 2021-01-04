from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import ReviewModel
import uuid


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
            code = '500'

        data = json.dumps({'code':code})        

        return Response(data, status = 200)
