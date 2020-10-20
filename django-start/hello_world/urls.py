from django.urls import path # create path objects
from hello_world import views # create app's views module

urlpatterns = [ # create a list of URL patterns that correspond to various URL functions
  	path('', views.hello_world, name="hello_world"), 
]

# only need to create one URL as we only have one function