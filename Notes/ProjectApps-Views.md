Intro
Now that you've created the projects to display on your portfolio site, you'll need to create view functions to send the data from the database to the HTML templates.
In the projects app, we'll create 2 views:
An index view that shows a snippet of information about each project
A detail view that shows more information on a particular topic/project

Index view
Inside views.py , we need to import the Project class from models.py and create a function project_index.py that renders a template called project_index.html 
 In the body of this function, you’ll make a Django ORM query to select all objects in the Project table:
from django.shortcuts import render
from projects.models import project

def project_index(request):
  projects = Projects.objects.all()
  context = {
    'projects': projects
  }
  return render(request, 'project_index.html`, context)
^^ Breaking it down:
In line 5 ( projects = Projects.objects.all() ) you perform a query
Query - a command that allows you to create, retrieve, update or delete objects/rows in your database
In this case, you're retrieving all objects in the projects table
A database query returns a collection of all objects that match the query - a queryset. In this case, you want all objects in the table, so it will return a collection of all projects
Line 6 - we define a dictionary context 
The dictionary only has one entry - projects - to which we assign our Queryset containing all projects
The context dictionary is used to send information to our template
Every view function you create needs to have a context dictionary
Line 9 - context is added as an argument to render() 
Any entries in the context dictionary are available in the template as long as the context argument is passed to render() 
You'll need to create a context dictionary and pass it to render in reach view function you create
We also render a template named project_index.html 
Doesn't exist yet
You'll create the templates for these views in the next section

Next - create the project_detail() view function. This function will need another argument - the id of the project that's being viewed
def project_detail(request, pk):
  project = Project.objects.get(pk=pk)
  context = {
    'project': project
  }
  return render(request, 'project_detail.html', context)

Line 2/14: project = Project.objects.get(pk=pk) -
We perform another query
Retrieves the project with primary key pk equal to that in the function argument
We then assign that project in our context dictionary which we pass to render() 
There's a template called project_detail.html - has not been created

Now that the view functions have been created we need to hook them up to URLs

URL Configuration: projects/urls.py :
from django.urls import path
from . import views

urlpatterns = [
  path("", views.project_index, name="project_index"),
  path("<int:pk>/", views.project_detail, name="project_detail",
]
^^
path("<int:pk>/", views.project_detail, name="project_detail", -
Contains all the URLs used in the project app
They are accessed when prefixed by projects/ 
There are now 2 full URLs that can be accessed with the project:
localhost:8000/projects: The project index page
localhost:8000/projects/3: The detail view for the project with pk=3 

These URLs won't work properly as there are no HTML templates
However, the view and logic are ready 
