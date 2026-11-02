from django.urls import path
from . import views

urlpatterns = [
    path('', views.fyrirspurn_view, name='fyrirspurn'),
    path('sent/', views.confirmation_view, name='confirmation'),
]