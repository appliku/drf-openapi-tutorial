from rest_framework import routers

from .api import *

router = routers.DefaultRouter()
router.register(r'task-lists', TaskListViewSet, basename='task-lists')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls
