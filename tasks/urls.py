from django.urls import path
from tasks.views import showTasks

urlpatterns = [
    path("show_tasks/", showTasks)
]