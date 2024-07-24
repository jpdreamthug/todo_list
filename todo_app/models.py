from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return f"{self.content}, created at - {self.created_at}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
