from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

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

def blog_category(request, category): # take a category name as an argument
    posts = Post.objects.filter( # query the post database for all posts that have been given the assigned category (assigned from the argument ^^)
        categories__name__contains=category # the name of the category has the category defined in the function/view definition argument/request
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

""" blog_category view
line 20 - Django queryset filter /#/ We only want posts who have been assigned a category that is equal to the one in the argument (i.e. the one the user has clicked on) // https://docs.djangoproject.com/en/2.1/topics/db/queries/#retrieving-specific-objects-with-filters
line 25 - add these posts and category to the context dictionary
line 29 - render our template for the category - blog_category.html """

def blog_detail(request, pk): # take the primary key of the post in the request as an argument for the link to be displayed
    post = Post.objects.get(pk=pk) # set the value for this post to be the post with the same pk as in the argument

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post) # get the comments for this post
    context = { # add the post and comments to our context to be displayed and then rendered to the blog_detail.html teplate in line 44
        "post": post,
        "comments": comments,
        "form": form;
    }

    return render(request, "blog_detail.html", context) # we need to add a form to the blog post details for submitting comments - see `form`