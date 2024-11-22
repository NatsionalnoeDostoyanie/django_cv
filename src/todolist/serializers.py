from rest_framework.serializers import ModelSerializer

from todolist.models.todo import Todo


class TodoSerializer(ModelSerializer[Todo]):
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "status", "created_at", "updated_at")
