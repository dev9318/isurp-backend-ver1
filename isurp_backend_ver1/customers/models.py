from djongo import models

# Create your models here.

class Address(models.Model):
    _id = models.ObjectIdField()
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
    _id = models.ObjectIdField()
    email = models.EmailField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    billing = models.EmbeddedField(
        model_container = Address
    )
    shipping = models.EmbeddedField(
        model_container = Address
    )
    isPayingCustomer = models.BooleanField()
    ordersCount = models.IntegerField()
    totalSpent = models.CharField(max_length=100)
    avatarUrl = models.CharField(max_length=255)
    guest = models.CharField(max_length=100)

