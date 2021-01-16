from djongo import models


DEFAULT_VALUE = ""

# Create your models here.

class Collection(models.Model):
    _id = models.ObjectIdField()
    href = models.CharField(max_length=100, default = DEFAULT_VALUE)


class Links(models.Model):
    _id = models.ObjectIdField()
    _self = models.ArrayField(model_container = Collection)
    collection =  models.ArrayField(model_container = Collection)



class Attribute(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    position = models.IntegerField()
    visible = models.BooleanField()
    variation = models.BooleanField()
#   List<String> options;

class DefaultAttribute(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # option = models.CharField(max_length=100, default = DEFAULT_VALUE)


class ProductImage(models.Model):
    _id = models.ObjectIdField()
    productId = models.CharField(max_length=100)
    dateCreated = models.DateTimeField()
    dateCreatedGmt = models.DateTimeField()
    dateModified = models.DateTimeField()
    dateModifiedGmt = models.DateTimeField()
    src = models.CharField(max_length=100, default = DEFAULT_VALUE)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
#   String alt;

class Dimensions(models.Model):
    _id = models.ObjectIdField()
    length = models.CharField(max_length=100, default = DEFAULT_VALUE)
    width = models.CharField(max_length=100, default = DEFAULT_VALUE)
    height = models.CharField(max_length=100, default = DEFAULT_VALUE)



class ProductCategory(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    slug = models.CharField(max_length=100, default = DEFAULT_VALUE)


class AvailableVariationImage(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100, default = DEFAULT_VALUE)
    url = models.CharField(max_length=100, default = DEFAULT_VALUE)
#   String src;
#   String fullSrc;


class Option(models.Model):
    _id = models.ObjectIdField()
    key = models.CharField(max_length=100, default = DEFAULT_VALUE)
    value = models.CharField(max_length=100, default = DEFAULT_VALUE)



class AvailableVariation(models.Model):
    _id = models.ObjectIdField()
    dimensions = models.EmbeddedField(model_container = Dimensions)
    displayPrice = models.DecimalField()
    displayRegularPrice = models.DecimalField()
    image = models.EmbeddedField(model_container = AvailableVariationImage)
    isInStock = models.BooleanField()
    isPurchasable = models.BooleanField()
    sku = models.CharField(max_length=100, default = DEFAULT_VALUE)
    variationDescription = models.CharField(max_length=100, default = DEFAULT_VALUE)
    variationId = models.IntegerField()
    option = models.ArrayField(model_container = Option)
    formattedPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    formattedSalesPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)


class VariationOption(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # List<String> options;
    attribute = models.CharField(max_length=100, default = DEFAULT_VALUE)
    selected = models.CharField(max_length=100, default = DEFAULT_VALUE)


class Product(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    slug = models.CharField(max_length=100, default = DEFAULT_VALUE)
    permalink = models.CharField(max_length=100, default = DEFAULT_VALUE)
    dateCreated = models.DateTimeField()
    dateCreatedGmt = models.DateTimeField()
    dateModified = models.DateTimeField()
    dateModifiedGmt = models.DateTimeField()
    type1 = models.CharField(max_length=100, default = 'variable')
    status = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # featured = models.BooleanField()
    # catalogVisibility = models.CharField(max_length=100, default = DEFAULT_VALUE)
    description = models.TextField()
    shortDescription = models.TextField()
    sku = models.CharField(max_length=100, default = DEFAULT_VALUE)
    price = models.CharField(max_length=100, default = DEFAULT_VALUE)
    regularPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    salePrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # dateOnSaleFrom = models.DateTimeField()
    # dateOnSaleFromGmt = models.DateTimeField()
    # dateOnSaleTo = models.DateTimeField()
    # dateOnSaleToGmt = models.DateTimeField()
    # priceHtml = models.CharField(max_length=100, default = DEFAULT_VALUE)
    onSale = models.BooleanField(default=False)
    # purchasable = models.BooleanField()
    totalSales = models.IntegerField()
    # virtual = models.BooleanField()
    #     downloadable = models.BooleanField()
    #   List<dynamic> downloads;
    #     downloadLimit = models.IntegerField()
    #     downloadExpiry = models.IntegerField()
    externalUrl = models.CharField(max_length=100, default = DEFAULT_VALUE)
    buttonText = models.CharField(max_length=100, default = DEFAULT_VALUE)
    taxStatus = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   taxClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   bool manageStock = models.BooleanField()
    stockQuantity = models.IntegerField()
    stockStatus = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   String backOrders = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   bool backordersAllowed = models.BooleanField()
    #   bool backordered = models.BooleanField()
    # soldIndividually = models.BooleanField()
    weight = models.CharField(max_length=100, default = DEFAULT_VALUE)
    dimensions = models.EmbeddedField(model_container= Dimensions)
    shippingRequired = models.BooleanField()
    #   bool shippingTaxable = models.BooleanField()
    # shippingClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # shippingClassId = models.IntegerField()
    reviewsAllowed = models.BooleanField()
    averageRating = models.CharField(max_length=100, default = DEFAULT_VALUE)
    ratingCount = models.IntegerField()
    # List<int> relatedIds
    # List<dynamic> upsellIds
    # List<dynamic> crossSellIds
    # parentId = models.IntegerField()
    # purchaseNote = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # categories = models.ArrayField(model_container = ProductCategory)
    #   List<dynamic> tags;
    images = models.ArrayField(model_container = ProductImage)
    # attributes = models.ArrayField(model_container = Attribute)
    # defaultAttributes =  models.ArrayField(model_container=DefaultAttribute)
    availableVariations = models.ArrayField(model_container=AvailableVariation)
    # List<dynamic> variations
    #   List<dynamic> groupedProducts;
    # menuOrder = models.IntegerField()
    #   List<dynamic> metaData;
    #   Links links;
    # decimals = models.IntegerField()
    vendor = models.CharField(max_length=100, default = DEFAULT_VALUE)

    objects = models.DjongoManager


class VendorReviews(models.Model):
    _id = models.ObjectIdField()
    vendorId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    authorId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    authorName = models.CharField(max_length=100, default = DEFAULT_VALUE)
    authorEmail = models.CharField(max_length=100, default = DEFAULT_VALUE)
    reviewTitle = models.CharField(max_length=100, default = DEFAULT_VALUE)
    reviewDescription = models.CharField(max_length=100, default = DEFAULT_VALUE)
    reviewRating = models.CharField(max_length=100, default = DEFAULT_VALUE)
    approved = models.CharField(max_length=100, default = DEFAULT_VALUE)
    created = models.DateTimeField()


class Address(models.Model):
    _id = models.ObjectIdField()
    street1 = models.TextField()
    street2 = models.TextField()
    city = models.CharField(max_length=100, default = DEFAULT_VALUE)
    _zip = models.CharField(max_length=100, default = DEFAULT_VALUE)
    country = models.CharField(max_length=100, default = DEFAULT_VALUE)
    state = models.CharField(max_length=100, default = DEFAULT_VALUE)


class StoreModel(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    icon = models.CharField(max_length=100, default = DEFAULT_VALUE)
    banner = models.CharField(max_length=100, default = DEFAULT_VALUE)
    address = models.EmbeddedField(model_container = Address)
    description = models.TextField()
    latitude = models.CharField(max_length=100, default = DEFAULT_VALUE)
    longitude = models.CharField(max_length=100, default = DEFAULT_VALUE)
    averageRating = models.DecimalField()
    ratingCount = models.IntegerField()
    productsCount = models.IntegerField()

