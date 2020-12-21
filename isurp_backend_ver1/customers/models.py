from djongo import models

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


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=100)
    # _id = models.ObjectIdField()
    email = models.EmailField()
    firstName = models.CharField(max_length=100, default = DEFAULT_VALUE)
    lastName = models.CharField(max_length=100, default = DEFAULT_VALUE)
    role = models.CharField(max_length=100, default = DEFAULT_VALUE)
    username = models.CharField(max_length=100, default = DEFAULT_VALUE)
    billing = models.EmbeddedField(
        model_container = Address
    )
    shipping = models.EmbeddedField(
        model_container = Address
    )
    isPayingCustomer = models.BooleanField()
    ordersCount = models.IntegerField()
    totalSpent = models.CharField(max_length=100, default = DEFAULT_VALUE)
    avatarUrl = models.CharField(max_length=100, default = DEFAULT_VALUE)
    guest = models.CharField(max_length=100, default = DEFAULT_VALUE)

