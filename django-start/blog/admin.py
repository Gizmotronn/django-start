from django.contrib import admin
from blog.models import Post, Category, Comment # import the models you want registered on the admin page

class PostAdmin(admin.ModelAdmin): # define empty class
    pass # don’t need to add any attributes or methods to these classes. They are used to customize what is shown on the admin pages. For this tutorial, the default configuration is enough.

class CategoryAdmin(admin.ModelAdmin): 
    pass

admin.site.register(Post, PostAdmin) # Post model - register model with the admin class
admin.site.register(Category, CategoryAdmin) # Category