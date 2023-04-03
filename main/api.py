from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from main.serializers import TaskListSerializer, TaskSerializer
from . import models


class TaskListViewSet(ModelViewSet):
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.TaskList.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return models.Task.objects.filter(task_list__owner=self.request.user)
