from django.shortcuts import render
from .models import Staff

def umokkur_view(request):
    staff_members = Staff.objects.all()
    return render(request, 'umokkur/umokkur.html', {'staff_members': staff_members})