from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'PortfolioApp/index.html', {'projects': projects})
