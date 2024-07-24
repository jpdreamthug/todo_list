from django.shortcuts import render
from django.views.generic import ListView

from todo_app.models import Task, Tag


class TasksListView(ListView):
    model = Task
    template_name = "todo_app/index.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related("tags")


class TagsListView(ListView):
    model = Tag
