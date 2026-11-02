
from django.shortcuts import render
from .models import Project

def verkefni_view(request):
    projects = Project.objects.order_by('-rodun')
    return render(request, 'verkefni/verkefni.html', {'projects': projects})