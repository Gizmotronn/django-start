"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # import Django admin from contrib
from django.urls import path, include # import django path, include for url management from django[.urls]

urlpatterns = [ # the path [+] setup for the urls
    path("admin/", admin.site.urls), # create a path called "admin" that uses 'admin.site.urls'
    path("projects/", include("projects.urls")), # create a path called "projects" which uses the "projects.urls" specified in the 'projects' app urls.py file
    # path('', include('hello_world.urls')),
]
