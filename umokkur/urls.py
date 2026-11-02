from django.urls import path
from . import views

urlpatterns = [
    path('', views.umokkur_view, name='umokkur'),
]
