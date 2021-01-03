from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Product

# Create your views here.


class fetch_products():

    def post(self, request):

        product_query = Product.objects.all()
        data = []
        for i in range(len(product_query)):

            data.append({
            'id': product_query[i]._id,
            'name': product_query[i].name,
            'type': product_query[i].type1,
            'status': product_query[i].status,
            'featured': product_query[i].featured,
            'catalogVisibility': product_query[i].catalogVisibility,
            'description': product_query[i].description,
            'shortDescription': product_query[i].shortDescription,
            'permalink': product_query[i].permalink,
            'sku': product_query[i].sku,
            'formattedPrice': product_query[i].formattedPrice,
            'formattedSalesPrice': product_query[i].formated_sales_price,
            'price': product_query[i].price,
            'regularPrice': product_query[i].regularPrice,
            'salePrice': product_query[i].salePrice,
            'onSale': product_query[i].onSale,
            'purchasable': product_query[i].purchasable,
            'totalSales': product_query[i].totalSales,
            'externalUrl': product_query[i].externalUrl,
            'buttonText': product_query[i].buttonText,
            'stockStatus': product_query[i].stockStatus,
            'weight': product_query[i].weight,
            'dimensions': product_query[i].dimensions,
            'reviewsAllowed': product_query[i].reviewsAllowed,
            'averageRating': product_query[i].averageRating,
            'ratingCount': product_query[i].ratingCount,
            'images': product_query[i].images,
            'availableVariations': product_query[i].availableVariations,
            'vendor': product_query[i].vendor,
            })
            # 'attributes': product_query[i].attributes,
            # 'categories': product_query[i].categories,
            # 'metaData': json["meta_data"] == null ? null : List<MetaDatum>.from(json["meta_data"].map((x) => MetaDatum.fromJson(x))),
        
        response = json.dumps(data)

        return Response(response, status = 200)


class get_product(APIView):

    def post(self,request):

        pid = request.data.get('product_id')

        pid = int(pid)
        
        try:
            product_query = Product.objects.get(_id = pid)
            data = {
            'id': product_query._id,
            'name': product_query.name,
            'type': product_query.type1,
            'status': product_query.status,
            'featured': product_query.featured,
            'catalogVisibility': product_query.catalogVisibility,
            'description': product_query.description,
            'shortDescription': product_query.shortDescription,
            'permalink': product_query.permalink,
            'sku': product_query.sku,
            'formattedPrice': product_query.formattedPrice,
            'formattedSalesPrice': product_query.formated_sales_price,
            'price': product_query.price,
            'regularPrice': product_query.regularPrice,
            'salePrice': product_query.salePrice,
            'onSale': product_query.onSale,
            'purchasable': product_query.purchasable,
            'totalSales': product_query.totalSales,
            'externalUrl': product_query.externalUrl,
            'buttonText': product_query.buttonText,
            'stockStatus': product_query.stockStatus,
            'weight': product_query.weight,
            'dimensions': product_query.dimensions,
            'reviewsAllowed': product_query.reviewsAllowed,
            'averageRating': product_query.averageRating,
            'ratingCount': product_query.ratingCount,
            'images': product_query.images,
            'availableVariations': product_query.availableVariations,
            'vendor': product_query.vendor,
            }

            code = 200

        except:
            code = 400

            data = {'message': 'some error occured'}

        response = json.dumps(data)
        return Response(response, status= code)


class get_product_sku(APIView):

    def post(self,request):

        pid = request.data.get('sku')

        
        try:
            product_query = Product.objects.get(sku = pid)

            data = {
            'id': product_query._id,
            'name': product_query.name,
            'type': product_query.type1,
            'status': product_query.status,
            'featured': product_query.featured,
            'catalogVisibility': product_query.catalogVisibility,
            'description': product_query.description,
            'shortDescription': product_query.shortDescription,
            'permalink': product_query.permalink,
            'sku': product_query.sku,
            'formattedPrice': product_query.formattedPrice,
            'formattedSalesPrice': product_query.formated_sales_price,
            'price': product_query.price,
            'regularPrice': product_query.regularPrice,
            'salePrice': product_query.salePrice,
            'onSale': product_query.onSale,
            'purchasable': product_query.purchasable,
            'totalSales': product_query.totalSales,
            'externalUrl': product_query.externalUrl,
            'buttonText': product_query.buttonText,
            'stockStatus': product_query.stockStatus,
            'weight': product_query.weight,
            'dimensions': product_query.dimensions,
            'reviewsAllowed': product_query.reviewsAllowed,
            'averageRating': product_query.averageRating,
            'ratingCount': product_query.ratingCount,
            'images': product_query.images,
            'availableVariations': product_query.availableVariations,
            'vendor': product_query.vendor,
            }
            
            code = 200

        except:
            code = 400

            data = {'message': 'some error occured'}

        response = json.dumps(data)
        return Response(response, status= code)

        