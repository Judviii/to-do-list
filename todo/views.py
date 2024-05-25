from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Task, Tag
from .forms import TaskForm


class IndexView(generic.ListView):
    """View function for the home page of the site."""
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by(*self.ordering)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    queryset = Task.objects.order_by("is_done", "-created_at")
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskDetailView(generic.DetailView):
    model = Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    queryset = Tag.objects.order_by("name")
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TagDetailView(generic.DetailView):
    model = Tag


class ToggleTaskStatus(View):
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse_lazy("todo:index"))
