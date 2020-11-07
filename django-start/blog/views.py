from django.shortcuts import render
from blog.models import Post, Comment

def blog_index(request):
	posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


""" blog_index view
`line 2` → import the `Post` & `Comment` modules (aka models) from the blog models

`line 5` → obtain a queryset containing all posts in the database. `order_by` orders the Queryset according to the **argument** (the date the post was created) given. The `-` tells Django to start with the **largest** value. 

`line 6` → define the context dictionary and render the template `blog_index.html`
"""