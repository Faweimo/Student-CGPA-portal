from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='overall_best'),
]