from djongo import models

# Create your models here.
class order(models.Model):
    id = models.AutoField(primary_key=True)
    int parentId;
    number = models.CharField(max_length=100, default = DEFAULT_VALUE)
    orderKey = models.CharField(max_length=100, default = DEFAULT_VALUE)
    createdVia = models.CharField(max_length=100, default = DEFAULT_VALUE)
    version = models.CharField(max_length=100, default = DEFAULT_VALUE)
    status = models.CharField(max_length=100, default = DEFAULT_VALUE)
    currency = models.CharField(max_length=100, default = DEFAULT_VALUE)
    DateTime dateCreated;
    DateTime dateCreatedGmt;
    DateTime dateModified;
    DateTime dateModifiedGmt;
    discountTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    discountTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    String shippingTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    String shippingTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    String cartTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    String total = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
  bool pricesIncludeTax;
  int customerId;
  String customerIpAddress = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String customerUserAgent = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String customerNote = models.CharField(max_length=100, default = DEFAULT_VALUE)
  Address billing;
  Address shipping;
  String paymentMethod = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String paymentMethodTitle = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String transactionId = models.CharField(max_length=100, default = DEFAULT_VALUE)
  dynamic datePaid;
  dynamic datePaidGmt;
  dynamic dateCompleted;
  dynamic dateCompletedGmt;
  String cartHash = models.CharField(max_length=100, default = DEFAULT_VALUE)
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
  String name = models.CharField(max_length=100, default = DEFAULT_VALUE)
  int productId;
  int variationId;
  int quantity;
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
  String methodTitle = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String methodId = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String instanceId = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String total = models.CharField(max_length=100, default = DEFAULT_VALUE)
  String totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
  List<dynamic> taxes 
#   List<MetaDatum> metaData;



  