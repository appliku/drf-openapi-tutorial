from django.contrib import admin
from .models import TaskList, Task


class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


admin.site.register(TaskList, TaskListAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_done', 'task_list')


admin.site.register(Task, TaskAdmin)
