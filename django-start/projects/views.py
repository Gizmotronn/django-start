from django.shortcuts import render # import render CLASS from Django shortcuts module
from projects.models import Project # Import Models CLASS (db/sql3) from Project Models

def project_index(request): # define the project_index class (using request as a param/parent)
    projects = Project.objects.all() # set what projects (like a variable) is - all projects // # query to select all objects in the `Project/#` table
    context = { # Makes use of the Django ORM // Define dictionary `context` :-> The dictionary only has one entry `projects` to which we assign our Queryset containing all projects. The context dictionary is used to send information to our template. Every view function you create needs to have a context dictionary.
        'projects': projects 
    }
    return render(request, 'project_index.html', context) # In line 9, context is added as an argument to render(). Any entries in the context dictionary are available in the template, as long as the context argument is passed to render(). You’ll need to create a context dictionary and pass it to render in each view function you create.
