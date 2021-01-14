from djongo import models
from isurp_backend_ver1.carts.models import CartModel

# Create your models here.

DEFAULT_VALUE = ""

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    # _id = models.ObjectIdField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

class LineItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default = DEFAULT_VALUE)
    productId = models.IntegerField()
    variationId = models.IntegerField()
    quantity = models.IntegerField()
    taxClass = models.CharField(max_length=100, default = DEFAULT_VALUE)
    subtotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    subtotalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    total = models.CharField(max_length=100, default = DEFAULT_VALUE)
    totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    taxes = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # List<dynamic> taxes = 
    #   List<LineItemMetaDatum> metaData;
    sku = models.CharField(max_length=100, default = DEFAULT_VALUE)
    price = models.DecimalField()



class ShippingLine(models.Model):
    id = models.AutoField(primary_key=True)
    methodTitle = models.CharField(max_length=100, default = DEFAULT_VALUE)
    methodId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    instanceId = models.CharField(max_length=100, default = DEFAULT_VALUE)
    total = models.CharField(max_length=100, default = DEFAULT_VALUE)
    totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    taxes = models.CharField(max_length=100, default = DEFAULT_VALUE)
    # List<dynamic> taxes 
#   List<MetaDatum> metaData;


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    parentId = models.IntegerField()
    number = models.CharField(max_length=100, default = DEFAULT_VALUE)
    orderKey = models.CharField(max_length=100, default = DEFAULT_VALUE)
    createdVia = models.CharField(max_length=100, default = DEFAULT_VALUE)
    version = models.CharField(max_length=100, default = DEFAULT_VALUE)
    status = models.CharField(max_length=100, default = DEFAULT_VALUE)
    currency = models.CharField(max_length=100, default = DEFAULT_VALUE)
    dateCreated = models.DateTimeField()
    dateCreatedGmt = models.DateTimeField()
    dateModified = models.DateTimeField()
    dateModifiedGmt = models.DateTimeField()
    discountTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    discountTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    shippingTotal = models.CharField(max_length=100, default = DEFAULT_VALUE)
    shippingTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    cartTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    total = models.CharField(max_length=100, default = DEFAULT_VALUE)
    totalTax = models.CharField(max_length=100, default = DEFAULT_VALUE)
    pricesIncludeTax = models.BooleanField()
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
    lineItems = models.ArrayField(
        model_container = LineItem
    )
    # List<dynamic> taxLines;
    shippingLines = models.ArrayField(
        model_container = ShippingLine
    )
    # List<dynamic> feeLines;
    #   List<dynamic> couponLines;
    # List<dynamic> refunds
    cartModel = models.EmbeddedField(model_container = CartModel)
    decimals = models.IntegerField()
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=100)
    objects = models.DjongoManager()