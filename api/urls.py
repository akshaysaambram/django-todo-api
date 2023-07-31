from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo-list'),
    path('todos/create/', views.todo_create, name='todo-create'),
    path('todos/<int:pk>/', views.todo_detail, name='todo-detail'),
]
