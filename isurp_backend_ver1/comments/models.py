from djongo import models



DEFAULT_VALUE = ''

# Create your models here.


# class Content(models.Model):
#     rendered = models.CharField(max_length=100, default = DEFAULT_VALUE)


# class Collection(models.Model):
#     href = models.CharField(max_length=100, default = DEFAULT_VALUE)

# class Author(models.Model):
#     embeddable = models.BooleanField()
#     href = models.CharField(max_length=100, default = DEFAULT_VALUE)


# class Up(models.Model):
#     embeddable = models.BooleanField()
#     postType = models.CharField(max_length=100, default = DEFAULT_VALUE)
#     href = models.CharField(max_length=100, default = DEFAULT_VALUE)


# class Links(models.Model):
#     self = models.ArrayField(model_container = Collection)
#     collection = models.ArrayField(model_container = Collection)
#     author = models.ArrayField(model_container = Author)
#     up = models.ArrayField(model_container = Up)



# class Comment(models.Model):
#     _id = models.ObjectIdField()
#     post = models.IntegerField()
#     parent = models.IntegerField()
#     author= models.IntegerField()
#     authorName = models.CharField(max_length=100, default = DEFAULT_VALUE)
#     authorUrl = models.CharField(max_length=100, default = DEFAULT_VALUE)
#     date = models.DateTimeField()
#     dateGmt = models.DateTimeField()
#     content = models.EmbeddedField(model_container = Content)
#     link = models.CharField(max_length=100, default = DEFAULT_VALUE)
#     status = models.CharField(max_length=100, default = DEFAULT_VALUE)
#     type = models.CharField(max_length=100, default = DEFAULT_VALUE)
#     # Map<String, String> authorAvatarUrls;
#     # List<dynamic> meta;
#     links = models.EmbeddedField(model_container = Links)


class ReviewModel(models.Model):
    id = models.CharField(max_length=100, default = DEFAULT_VALUE)
    author = models.CharField(max_length=100, default = DEFAULT_VALUE)
    email = models.CharField(max_length=100, default = DEFAULT_VALUE)
    content = models.CharField(max_length=100, default = DEFAULT_VALUE)
    rating = models.CharField(max_length=100, default = DEFAULT_VALUE)
    avatar = models.CharField(max_length=100, default = DEFAULT_VALUE)
    date = models.DateTimeField()

    objects = models.DjongoManager