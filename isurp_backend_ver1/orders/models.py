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
    String shippingTotal;
    String shippingTax;
    String cartTax;
    String total;
  String totalTax;
  bool pricesIncludeTax;
  int customerId;
  String customerIpAddress;
  String customerUserAgent;
  String customerNote;
  Address billing;
  Address shipping;
  String paymentMethod;
  String paymentMethodTitle;
  String transactionId;
  dynamic datePaid;
  dynamic datePaidGmt;
  dynamic dateCompleted;
  dynamic dateCompletedGmt;
  String cartHash;
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
  String name;
  int productId;
  int variationId;
  int quantity;
  String taxClass;
  String subtotal;
  String subtotalTax;
  String total;
  String totalTax;
  List<dynamic> taxes;
#   List<LineItemMetaDatum> metaData;
  String sku;
  double price;



  class ShippingLine(models.Model):
    id = models.AutoField(primary_key=True)
  String methodTitle;
  String methodId;
  String instanceId;
  String total;
  String totalTax;
  List<dynamic> taxes;
#   List<MetaDatum> metaData;



  