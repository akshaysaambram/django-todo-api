from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todos/create/', views.create, name='todo-create'),
    path('todos/todo/<int:pk>/', views.detail, name='todo-detail'),
    path('todos/update/<int:pk>/', views.update_view, name='todo-update'),
    path('todos/delete/<int:pk>/', views.delete_view, name='todo-delete'),
]