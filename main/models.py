from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_lists')

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
