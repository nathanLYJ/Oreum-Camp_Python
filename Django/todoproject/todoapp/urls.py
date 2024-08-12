from django.urls import path
from . import views

urlpatterns = [
	path("", views.task_list, name="task_list"),
	path("add/", views.add_task, name="add_task"),
	path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
	path('set_priority/<int:task_id>/', views.set_priority, name='set_priority'),
	path('statistics/', views.task_statistics, name='task_statistics'),
]