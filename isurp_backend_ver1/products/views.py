from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Product

# Create your views here.


class fetch_products():

    def post(self, request):

        
        data = {
        'id': json["id"] == null ? null : json["id"],
        'name': json["name"] == null ? null : json["name"],
        'type': json["type"] == null ? null : json["type"],
        'status': json["status"] == null ? null : json["status"],
        'featured': json["featured"] == null ? null : json["featured"],
        'catalogVisibility': json["catalog_visibility"] == null ? null : json["catalog_visibility"],
        'description': json["description"] == null ? null : json["description"],
        'shortDescription': json["short_description"] == null ? null : json["short_description"],
        'permalink': json["permalink"] == null ? null : json["permalink"],
        'sku': json["sku"] == null ? null : json["sku"],
        formattedPrice: json["formated_price"] == null ? null : json["formated_price"],
        formattedSalesPrice: json["formated_sales_price"] == null ? null : json["formated_sales_price"],
        price: json["price"] == null ? null : json["price"].toDouble(),
        regularPrice: json["regular_price"] == null ? null : json["regular_price"].toDouble(),
        salePrice: json["sale_price"] == null ? null : json["sale_price"].toDouble(),
        onSale: json["on_sale"] == null ? null : json["on_sale"],
        purchasable: json["purchasable"] == null ? null : json["purchasable"],
        totalSales: json["total_sales"] == null ? null : json["total_sales"],
        virtual: json["virtual"] == null ? null : json["virtual"],
        downloadable: json["downloadable"] == null ? null : json["downloadable"],
        externalUrl: json["external_url"] == null ? null : json["external_url"],
        buttonText: json["button_text"] == null ? null : json["button_text"],
        manageStock: json["manage_stock"] == null ? null : json["manage_stock"],
        stockQuantity: json["stock_quantity"] == null ? null : json["stock_quantity"],
        stockStatus: json["stock_status"] == null ? null : json["stock_status"],
        backorders: json["backorders"] == null ? null : json["backorders"],
        backordersAllowed: json["backorders_allowed"] == null ? null : json["backorders_allowed"],
        backordered: json["backordered"] == null ? null : json["backordered"],
        soldIndividually: json["sold_individually"] == null ? null : json["sold_individually"],
        weight: json["weight"] == null ? null : json["weight"],
        dimensions: json["dimensions"] == null ? null : Dimensions.fromJson(json["dimensions"]),
        reviewsAllowed: json["reviews_allowed"] == null ? null : json["reviews_allowed"],
        averageRating: json["average_rating"] == null ? null : json["average_rating"],
        ratingCount: json["rating_count"] == null ? null : json["rating_count"],
        relatedIds: json["related_ids"] == null ? null : List<int>.from(json["related_ids"].map((x) => x)),
        upsellIds: json["upsell_ids"] == null ? null : List<int>.from(json["upsell_ids"].map((x) => x)),
        crossSellIds: json["cross_sell_ids"] == null ? null : List<int>.from(json["cross_sell_ids"].map((x) => x)),
        purchaseNote: json["purchase_note"] == null ? null : json["purchase_note"],
        categories: json["categories"] == null ? [] :  List<int>.from(json["categories"].map((x) => x)),
        tags: json["tags"] == null ? null : List<dynamic>.from(json["tags"].map((x) => x)),
        images: json["images"] == null ? null : List<Mage>.from(json["images"].map((x) => Mage.fromJson(x))),
        attributes: json["attributes"] == null ? null : List<Attribute>.from(json["attributes"].map((x) => Attribute.fromJson(x))),
        groupedProducts: json["grouped_products"] == null ? null : List<dynamic>.from(json["grouped_products"].map((x) => x)),
        metaData: json["meta_data"] == null ? null : List<MetaDatum>.from(json["meta_data"].map((x) => MetaDatum.fromJson(x))),
        availableVariations: json["availableVariations"] == null ? null : List<AvailableVariation>.from(json["availableVariations"].map((x) => AvailableVariation.fromJson(x))),
        variationOptions: json["variationOptions"] == null ? null : List<VariationOption>.from(json["variationOptions"].map((x) => VariationOption.fromJson(x))),
        vendor: json["vendor"] == null ? null : Vendor.fromJson(json["vendor"]),
        children: json['children'] == null ? null : List<Product>.from(json["children"].map((x) => Product.fromJson(x))),
        }