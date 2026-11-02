
from django.urls import path
from .views import verkefni_view

urlpatterns = [
    path('', verkefni_view, name='verkefni'),
]