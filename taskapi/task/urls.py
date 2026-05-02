from django.urls import path
from . import views

from django.http import HttpResponse

def home(request):
    return HttpResponse("Task API is running")

urlpatterns = [
    path('', home),
    path('task/', views.get_task),
    path('task/create/', views.create_task),
    path('task/update/<int:pk>/', views.update_task),
    path('task/delete/<int:pk>/', views.delete_task),
]