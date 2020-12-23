from djongo import models

# Create your models here.


class Product(models.Model):
    int id;
    productId = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    slug = models.CharField(max_length=100, default = DEFAULT_VALUE)
    permalink = models.CharField(max_length=100, default = DEFAULT_VALUE)
    dateCreated = models.DateTimeField()
    dateCreatedGmt = models.DateTimeField()
    dateModified = models.DateTimeField()
    dateModifiedGmt = models.DateTimeField()
    type = models.CharField(max_length=100, default = DEFAULT_VALUE)
    status = models.CharField(max_length=100, default = DEFAULT_VALUE)
    featured = models.BooleanField()
    catalogVisibility = models.CharField(max_length=100, default = DEFAULT_VALUE)
    description = models.TextField()
    shortDescription = models.TextField()
    sku = models.CharField(max_length=100, default = DEFAULT_VALUE)
    price = models.CharField(max_length=100, default = DEFAULT_VALUE)
    regularPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    salePrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    dateOnSaleFrom = models.DateTimeField()
    dateOnSaleFromGmt = models.DateTimeField()
    dateOnSaleTo = models.DateTimeField()
    dateOnSaleToGmt = models.DateTimeField()
    priceHtml = models.CharField(max_length=100, default = DEFAULT_VALUE)
    onSale = models.BooleanField()
    purchasable = models.BooleanField()
    totalSales = models.IntegerField()
    virtual = models.BooleanField()
    #     downloadable = models.BooleanField()
    #   List<dynamic> downloads;
    #     downloadLimit = models.IntegerField()
    #     downloadExpiry = models.IntegerField()
  String externalUrl = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String buttonText = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String taxStatus = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String taxClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool manageStock = models.BooleanField()
  int stockQuantity = models.IntegerField()
  String stockStatus = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String backOrders = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool backordersAllowed = models.BooleanField()
  bool backordered = models.BooleanField()
  bool soldIndividually = models.BooleanField()
  String weight = models.CharField(max_length=100, default = DEFAULT_VALUE)
  Dimensions dimensions;
  bool shippingRequired = models.BooleanField()
  bool shippingTaxable = models.BooleanField()
  String shippingClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
  int shippingClassId = models.IntegerField()
  bool reviewsAllowed = models.BooleanField()
  String averageRating = models.CharField(max_length=100, default = DEFAULT_VALUE)
  int ratingCount = models.IntegerField()
  List<int> relatedIds;
  List<dynamic> upsellIds;
  List<dynamic> crossSellIds;
  int parentId = models.IntegerField()
  String purchaseNote = models.CharField(max_length=100, default = DEFAULT_VALUE)
  List<ProductCategory> categories;
  List<dynamic> tags;
  List<ProductImage> images;
  List<Attribute> attributes;
  List<DefaultAttribute> defaultAttributes;
  List<dynamic> variations;
#   List<dynamic> groupedProducts;
  int menuOrder = models.IntegerField()
#   List<dynamic> metaData;
  Links links;
  int decimals = models.IntegerField()
  String vendor = models.CharField(max_length=100, default = DEFAULT_VALUE)



class Dimensions(models.Model):
    length = models.CharField(max_length=100, default = DEFAULT_VALUE)
    width = models.CharField(max_length=100, default = DEFAULT_VALUE)
    height = models.CharField(max_length=100, default = DEFAULT_VALUE)

class ProductImage(models.Model):
    int id;
    productId = models.CharField(max_length=100)
    DateTime dateCreated = models.DateTimeField()
    DateTime dateCreatedGmt = models.DateTimeField()
    DateTime dateModified = models.DateTimeField()
    DateTime dateModifiedGmt = models.DateTimeField()
    src = models.CharField(max_length=100, default = DEFAULT_VALUE)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
#   String alt;


class ProductCategory(models.Model):
    int id;
    String name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    slug = models.CharField(max_length=100, default = DEFAULT_VALUE)