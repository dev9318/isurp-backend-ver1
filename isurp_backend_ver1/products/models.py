from djongo import models

# Create your models here.


class Product(models.Model):
    int id;
    productId = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    slug = models.CharField(max_length=100, default = DEFAULT_VALUE)
    permalink = models.CharField(max_length=100, default = DEFAULT_VALUE)
  DateTime dateCreated;
  DateTime dateCreatedGmt;
  DateTime dateModified;
  DateTime dateModifiedGmt;
  String type = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String status = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool featured;
  String catalogVisibility = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String description = models.TextField()
  String shortDescription = models.TextField()
  String sku = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String price = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String regularPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String salePrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
  dynamic dateOnSaleFrom;
  dynamic dateOnSaleFromGmt;
  dynamic dateOnSaleTo;
  dynamic dateOnSaleToGmt;
  String priceHtml = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool onSale;
  bool purchasable;
  int totalSales;
  bool virtual;
  bool downloadable;
  List<dynamic> downloads;
  int downloadLimit;
  int downloadExpiry;
  String externalUrl = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String buttonText = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String taxStatus = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String taxClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool manageStock;
  int stockQuantity;
  String stockStatus = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String backOrders = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool backordersAllowed;
  bool backordered;
  bool soldIndividually;
  String weight = models.CharField(max_length=100, default = DEFAULT_VALUE)
  Dimensions dimensions;
  bool shippingRequired;
  bool shippingTaxable;
  String shippingClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
  int shippingClassId;
  bool reviewsAllowed;
  String averageRating = models.CharField(max_length=100, default = DEFAULT_VALUE)
  int ratingCount;
  List<int> relatedIds;
  List<dynamic> upsellIds;
  List<dynamic> crossSellIds;
  int parentId;
  String purchaseNote = models.CharField(max_length=100, default = DEFAULT_VALUE)
  List<ProductCategory> categories;
  List<dynamic> tags;
  List<ProductImage> images;
  List<Attribute> attributes;
  List<DefaultAttribute> defaultAttributes;
  List<dynamic> variations;
#   List<dynamic> groupedProducts;
  int menuOrder;
#   List<dynamic> metaData;
  Links links;
  int decimals;
  String vendor = models.CharField(max_length=100, default = DEFAULT_VALUE)



class Dimensions(models.Model):
    length = models.CharField(max_length=100, default = DEFAULT_VALUE)
    width = models.CharField(max_length=100, default = DEFAULT_VALUE)
    height = models.CharField(max_length=100, default = DEFAULT_VALUE)

class ProductImage(models.Model):
    #   int id;
    productId = models.CharField(max_length=100)
    DateTime dateCreated;
    DateTime dateCreatedGmt;
    DateTime dateModified;
    DateTime dateModifiedGmt;
    src = models.CharField(max_length=100, default = DEFAULT_VALUE)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
#   String alt;


