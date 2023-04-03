from rest_framework import serializers
from . import models


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskList
        fields = ('id', 'name',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'title', 'created_at', 'is_done', 'task_list')

    def validate_task_list(self, value):
        if self.context['request'].user != value.owner:
            raise serializers.ValidationError('Invalid task list')
        return value
