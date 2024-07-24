from django.contrib import admin

from todo_app.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline_time", "is_completed", "get_tags"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("tags")

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...
