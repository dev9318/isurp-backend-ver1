from djongo import models
from "isurp_backend_ver1\customers\models" import Address

# Create your models here.
class order(models.Model):
    id = models.AutoField(primary_key=True)
    parentId = models.IntegerField()
    number = models.CharField(max_length=100, default = DEFAULT_VALUE)
    orderKey = models.CharField(max_length=100, default = DEFAULT_VALUE)
    createdVia = models.CharField(max_length=100, default = DEFAULT_VALUE)
    version = models.CharField(max_length=100, default = DEFAULT_VALUE)
    status = models.CharField(max_length=100, default = DEFAULT_VALUE)
    currency = models.CharField(max_length=100, default = DEFAULT_VALUE)
    DateTime dateCreated = models.DateTimeField()
    DateTime dateCreatedGmt = models.DateTimeField()
    DateTime dateModified = models.DateTimeField()
    DateTime dateModifiedGmt = models.DateTimeField()
    discountTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    discountTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    shippingTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    shippingTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    cartTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    total = models.CharField(max_length=100, default = DEFAULT_VALUE)
    totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool pricesIncludeTax;
    customerId = models.IntegerField()
    customerIpAddress = models.CharField(max_length=100, default = DEFAULT_VALUE)
    customerUserAgent = models.CharField(max_length=100, default = DEFAULT_VALUE)
    customerNote = models.CharField(max_length=100, default = DEFAULT_VALUE)
    billing = models.EmbeddedField(
        model_container = Address
    )
    shipping = models.EmbeddedField(
        model_container = Address
    )
    paymentMethod = models.CharField(max_length=100, default = DEFAULT_VALUE)
    paymentMethodTitle = models.CharField(max_length=100, default = DEFAULT_VALUE)
    transactionId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    datePaid = models.DateTimeField()
    datePaidGmt = models.DateTimeField()
    dateCompleted = models.DateTimeField()
    dateCompletedGmt = models.DateTimeField()
    cartHash = models.CharField(max_length=100, default = DEFAULT_VALUE)
#   List<MetaDatum> metaData;
  List<LineItem> lineItems;
  List<dynamic> taxLines;
  List<ShippingLine> shippingLines;
  List<dynamic> feeLines;
#   List<dynamic> couponLines;
  List<dynamic> refunds;
  int decimals;



  class LineItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    productId = models.IntegerField()
    variationId = models.IntegerField()
    quantity = models.IntegerField()
  String taxClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String subtotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String subtotalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String total = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
  List<dynamic> taxes
#   List<LineItemMetaDatum> metaData;
  String sku = models.CharField(max_length=100, default = DEFAULT_VALUE)
  double price



  class ShippingLine(models.Model):
    id = models.AutoField(primary_key=True)
    methodTitle = models.CharField(max_length=100, default = DEFAULT_VALUE)
    methodId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    instanceId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    total = models.CharField(max_length=100, default = DEFAULT_VALUE)
    totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
  List<dynamic> taxes 
#   List<MetaDatum> metaData;



  