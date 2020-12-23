from djongo import models

# Create your models here.


class Comment(models.Model):
  int _id;
  int post;
  int parent;
  int author;
  String authorName;
  String authorUrl;
  DateTime date;
  DateTime dateGmt;
  Content content;
  String link;
  String status;
  String type;
  Map<String, String> authorAvatarUrls;
  List<dynamic> meta;
  Links links;