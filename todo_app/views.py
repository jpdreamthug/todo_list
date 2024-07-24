from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View

from todo_app.forms import TaskForm, TagForm
from todo_app.models import Task, Tag


class TaskListView(ListView):
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by(
            "is_completed",
            "-created_at"
        ).prefetch_related("tags")


class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy("todo_app:task-list")
    form_class = TaskForm


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo-app:task-list")


class TaskChangeStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect("todo_app:task-list")


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")
    form_class = TagForm


class TagUpdateView(UpdateView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")
    form_class = TagForm


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")
