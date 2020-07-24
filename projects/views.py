from django.shortcuts import render
from projects.models import project

def project_index(request):
  projects = Projects.objects.all()
  context = {
    'projects': projects
  }
  return render(request, 'project_index.html`, context)

def project_detail(request, pk):
  project = Project.objects.get(pk=pk)
  context = {
    'project': project
  }
  return render(request, 'project_detail.html', context)