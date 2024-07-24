from django.urls import path

from todo_app.views import TasksListView, TagsListView

urlpatterns = [
    path("", TasksListView.as_view(), name="index"),
    path("tags/", TagsListView.as_view(), name="tag-list")
]

app_name = "todo_app"
