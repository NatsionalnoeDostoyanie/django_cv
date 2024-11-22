from typing import cast

from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import ModelViewSet

from todolist.models.todo import Todo
from todolist.serializers import TodoSerializer


class TodoViewSet(ModelViewSet[Todo]):
    serializer_class = TodoSerializer

    def get_queryset(self) -> QuerySet[Todo]:
        # TODO: Consider removing `cast()` since `self.request.user` is guaranteed to be
        # an instance of `User` (not `AnonymousUser`) due to the `IsAuthenticated` permission class
        # (used for type checking)
        return Todo.objects.filter(
            owner=cast(settings.AUTH_USER_MODEL, self.request.user)  # type: ignore[name-defined]
        )

    def perform_create(self, serializer: BaseSerializer[Todo]) -> None:
        serializer.save(owner=self.request.user)
