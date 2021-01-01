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
            'formattedPrice': product_query[i].fo,
            'formattedSalesPrice': json["formated_sales_price"] == null ? null : json["formated_sales_price"],
            'price': product_query[i].price,
            'regularPrice': product_query[i].regularPrice,
            'salePrice': product_query[i].salePrice,
            'onSale': product_query[i].onSale,
            'purchasable': product_query[i].purchasable,
            'totalSales': product_query[i].totalSales,
            'virtual': product_query[i].virtual,
            'downloadable': ,
            'externalUrl': product_query[i].externalUrl,
            'buttonText': product_query[i].buttonText,
            'stockStatus': ,
            'soldIndividually': product_query[i].soldIndividually,
            'weight': product_query[i].weight,
            'dimensions': product_query[i].dimensions,
            'reviewsAllowed': product_query[i].reviewsAllowed,
            'averageRating': product_query[i].averageRating,
            'ratingCount': product_query[i].ratingCount,
            'relatedIds': ,
            'upsellIds': ,
            'crossSellIds': ,
            'purchaseNote': ,
            'categories': product_query[i].categories,
            'tags': ,
            'images': product_query[i].images,
            'attributes': product_query[i].attributes,
            'groupedProducts': ,
            'availableVariations': ,
            'variationOptions': ,
            'vendor': product_query[i].vendor,
            'children': ,
            })
            # 'metaData': json["meta_data"] == null ? null : List<MetaDatum>.from(json["meta_data"].map((x) => MetaDatum.fromJson(x))),
        
        response = json.dumps(data)

        return Response(response, status = 200)


class get_product(APIView):

    def post(self,request):

        pid = request.data.get('product_id')

        pid = int(pid)'
        
        try:
            product_query = Product.objects.get(_id = pid)


            '


class get_product_sku(APIView):

    def post(self,request):

        pid = request.data.get('sku')

        
        try:
            product_query = Product.objects.get(sku = pid)



            
            '