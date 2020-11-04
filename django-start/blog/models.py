from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=20)

class Post(models.Model):
	title = models.CharField(max_length=255)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  categories = models.ManyToManyField('Category', related_name='posts')