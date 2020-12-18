from djongo import models

# Create your models here.

class CartFee(models.Model):
    Id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    total = models.CharField(max_length=100)


class CartContent(models.Model):
#   List<dynamic> addons;
    String key = models.CharField(max_length=100)
    productId = models.IntegerField()
    variationId = models.IntegerField()
    # dynamic variation;
    quantity = models.IntegerField()
    dataHash = models.CharField(max_length=100)
#   //LineTaxData lineTaxData;
    # double lineSubtotal = models.CharField(max_length=100)
    # double lineSubtotalTax = models.CharField(max_length=100)
    # double lineTotal = models.CharField(max_length=100)
    # double lineTax = models.CharField(max_length=100)
#   Data data;
    name = models.CharField(max_length=100)
    thumb = models.CharField(max_length=100)
    removeUrl = models.CharField(max_length=100)
    price = models.DecimalField()
    taxPrice = models.DecimalField()
    regularPrice = models.DecimalField()
    salesPrice = models.DecimalField()
    loadingQty =  models.BooleanField()
    formattedPrice = models.CharField(max_length=100)
    formattedSalesPrice = models.CharField(max_length=100)
    parentId = models.IntegerField()


# class Content(models.Model):
#   List<dynamic> addons;
#   String key;
#   int productId;
#   int variationId;
#   dynamic variation;
#   int quantity;
#   String dataHash;
#   LineTaxData lineTaxData;
#   int lineSubtotal;
#   int lineSubtotalTax;
#   int lineTotal;
#   int lineTax;
#   Data data;

# class Destination(models.Model):
#   String country;
#   String state;
#   String postcode;
#   String city;
#   String address;
#   String address2;

# class User(models.Model):
#   int id;


class CartTotals(models.Model):
    String subtotal = models.CharField(max_length=100)
    String subtotalTax = models.CharField(max_length=100)
    String shippingTotal = models.CharField(max_length=100)
    String shippingTax = models.CharField(max_length=100)
#   //List<dynamic> shippingTaxes;
    String discountTotal = models.CharField(max_length=100)
    String discountTax = models.CharField(max_length=100)
    String cartContentsTotal = models.CharField(max_length=100)
    String cartContentsTax = models.CharField(max_length=100)
#   //List<dynamic> cartContentsTaxes;
    String feeTotal = models.CharField(max_length=100)
    String feeTax = models.CharField(max_length=100)
#   //List<dynamic> feeTaxes;
    String total = models.CharField(max_length=100)
    String totalTax = models.CharField(max_length=100)


# class CartSessionData(models.Model):
#     cartContentsTotal = models.IntegerField()
#     total = models.IntegerField()
#   int subtotal;
#   int subtotalExTax;
#   int taxTotal;
#   List<dynamic> taxes;
#   List<dynamic> shippingTaxes;
#   int discountCart;
#   int discountCartTax;
#   int shippingTotal;
#   int shippingTaxTotal;
#   List<dynamic> couponDiscountAmounts;
#   List<dynamic> couponDiscountTaxAmounts;
#   int feeTotal;
#   List<dynamic> fees;


# class ShippingMethod(models.Model):
#   String id;
#   String label;
#   String cost;
#   String methodId;
#   List<dynamic> taxes;

class CartModel(models.Model):
  #List<dynamic> appliedCoupons;
    taxDisplayCart = models.CharField(max_length=100)
    # CartSessionData cartSessionData = 
  #List<dynamic> couponAppliedCount;
#   List<dynamic> couponDiscountTotals;
#   List<dynamic> couponDiscountTaxTotals;
    cartContents = models.ManyToManyField(CartContent)
    cartNonce = models.CharField(max_length=100)
    cartTotals = models.ManyToManyField(CartTotals)
#   List<dynamic> chosenShipping;
#   Points points;
#   int purchasePoint;
    currency = models.CharField(max_length=100)
    cartFees = models.ManyToManyField(CartFee)
#   List<Coupon> coupons;