from djongo import models


DEFAULT_VALUE = ''


# Create your models here.

class CartFee(models.Model):
    id = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    amount = models.CharField(max_length=100, default = DEFAULT_VALUE)
    total = models.CharField(max_length=100, default = DEFAULT_VALUE)


class CartContent(models.Model):
    #   List<dynamic> addons;
    key = models.CharField(max_length=100, default = DEFAULT_VALUE)
    productId = models.IntegerField()
    variationId = models.IntegerField()
    # dynamic variation;
    quantity = models.IntegerField()
    # dataHash = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   //LineTaxData lineTaxData;
    # double lineSubtotal = models.CharField(max_length=100)
    # double lineSubtotalTax = models.CharField(max_length=100)
    # double lineTotal = models.CharField(max_length=100)
    # double lineTax = models.CharField(max_length=100)
    #   Data data;
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    thumb = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # removeUrl = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # price = models.DecimalField()
    # taxPrice = models.DecimalField()
    # regularPrice = models.DecimalField()
    # salesPrice = models.DecimalField()
    loadingQty =  models.BooleanField()
    formattedPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # formattedSalesPrice = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # parentId = models.IntegerField()


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
    _id = models.AutoField(primary_key=True)
    subtotal = models.IntegerField(max_length=100, default = DEFAULT_VALUE)
    # subtotalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    shippingTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # shippingTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   //List<dynamic> shippingTaxes;
    discountTotal = models.IntegerField(max_length=100, default = DEFAULT_VALUE)
    # discountTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # cartContentsTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # cartContentsTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   //List<dynamic> cartContentsTaxes;
    # feeTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # feeTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    #   //List<dynamic> feeTaxes;
    total = models.IntegerField(max_length=100, default = DEFAULT_VALUE)
    totalTax = models.IntegerField(max_length=100, default = DEFAULT_VALUE)


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
    _id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    taxDisplayCart = models.CharField(max_length=100)
    # CartSessionData cartSessionData = 
    #List<dynamic> couponAppliedCount;
    #   List<dynamic> couponDiscountTotals;
    #   List<dynamic> couponDiscountTaxTotals;
    cartContents = models.ArrayField(model_container = CartContent)
    cartNonce = models.CharField(max_length=100, default = DEFAULT_VALUE)
    cartTotals = models.EmbeddedField(model_container = CartTotals)
    #   List<dynamic> chosenShipping;
    #   Points points;
    #   int purchasePoint;
    currency = models.CharField(max_length=100, default = 'INR')
    cartFees = models.ArrayField(model_container = CartFee)

    objects = models.DjongoManager()
    #   List<Coupon> coupons;
    def __str__(self):
        self.uid
