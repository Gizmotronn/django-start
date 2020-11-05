from django.db import models # import models from django (database) module

class Category(models.Model): # create a class (of type model) called Category
	name = models.CharField(max_length=20) # there's one field - name - and it is of type CharField with a max character length of 20

class Post(models.Model): # create a class (of type models) called Post
	title = models.CharField(max_length=255) # attribute/field called title with a max length of 225 characters (CharField)
  body = models.TextField() # attribute called body of type TextField - no max length
  created_on = models.DateTimeField(auto_now_add=True) # attribute for the date published
  last_modified = models.DateTimeField(auto_now=True) # attribute for when it was last edited (it = post)
  categories = models.ManyToManyField('Category', related_name='posts') # category attribute relating to 'category' model
	
class Comment(models.Model): # create a model called Comment
    author = models.CharField(max_length=60) # attribute for comment author
    body = models.TextField() # attribute for the body of the comment
    created_on = models.DateTimeField(auto_now_add=True) # time of comment
    post = models.ForeignKey('Post', on_delete=models.CASCADE) # attribute linking to the post
