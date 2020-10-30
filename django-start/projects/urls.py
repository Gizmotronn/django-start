from django.urls import path # import path from Django urls - module for file paths
from . import views # import views.py

urlpatterns = [ 
    path("", views.project_index, name="project_index"), # hook up the root URL of our APP to the `project_index` view
    path("<int:pk>/", views.project_detail, name="project_detail"), # hook up the `project_detail` view -> generate the URL (using the pk attribute) depending on which project[_detail] you want to view // To do this, we used the <int:pk> notation. This just tells Django that the value passed in the URL is an integer, and its variable name is pk.
]
