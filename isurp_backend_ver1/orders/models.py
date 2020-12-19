from djongo import models

# # Create your models here.
# class order(models.Model):
#     id;
#   int parentId;
#   String number;
#   String orderKey;
#   String createdVia;
#   String version;
#   String status;
#   String currency;
#   DateTime dateCreated;
#   DateTime dateCreatedGmt;
#   DateTime dateModified;
#   DateTime dateModifiedGmt;
#   String discountTotal;
#   String discountTax;
#   String shippingTotal;
#   String shippingTax;
#   String cartTax;
#   String total;
#   String totalTax;
#   bool pricesIncludeTax;
#   int customerId;
#   String customerIpAddress;
#   String customerUserAgent;
#   String customerNote;
#   Address billing;
#   Address shipping;
#   String paymentMethod;
#   String paymentMethodTitle;
#   String transactionId;
#   dynamic datePaid;
#   dynamic datePaidGmt;
#   dynamic dateCompleted;
#   dynamic dateCompletedGmt;
#   String cartHash;
#   List<MetaDatum> metaData;
#   List<LineItem> lineItems;
#   List<dynamic> taxLines;
#   List<ShippingLine> shippingLines;
#   List<dynamic> feeLines;
#   List<dynamic> couponLines;
#   List<dynamic> refunds;
#   int decimals;



#   class LineItem(models.Model):
#   int id;
#   String name;
#   int productId;
#   int variationId;
#   int quantity;
#   String taxClass;
#   String subtotal;
#   String subtotalTax;
#   String total;
#   String totalTax;
#   List<dynamic> taxes;
#   List<LineItemMetaDatum> metaData;
#   String sku;
#   double price;



#   class ShippingLine(models.Model):
#   int id;
#   String methodTitle;
#   String methodId;
#   String instanceId;
#   String total;
#   String totalTax;
#   List<dynamic> taxes;
#   List<MetaDatum> metaData;



  