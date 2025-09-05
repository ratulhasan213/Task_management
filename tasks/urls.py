from django.urls import path
from tasks.views import*

urlpatterns = [
    path("show_tasks/", showTasks),
    path("show_tasks/<int:id>/", showSpecificTasks) # here addded
]