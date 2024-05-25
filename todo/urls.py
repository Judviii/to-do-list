from django.urls import path
from .views import (
    IndexView,
    ToggleTaskStatus,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagDetailView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path(
        "toggle-task-status/<int:pk>/",
        ToggleTaskStatus.as_view(),
        name="toggle-task-status"
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "tasks/<int:pk>/detail/", TaskDetailView.as_view(), name="task-detail"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path(
        "tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"
    ),
    path(
        "tags/<int:pk>/detail/", TagDetailView.as_view(), name="tag-detail"
    ),
]

app_name = "todo"
