from django.urls import path
from . import views

urlpatterns = [
    path('', views.Task_list, name='Task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('mark_all_completed/', views.mark_all_completed, name='mark_all_completed'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('clear_completed/', views.clear_completed, name='clear_completed'),
]
