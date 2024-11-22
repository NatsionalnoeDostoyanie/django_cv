from django.conf import settings
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextChoices,
    TextField,
)


class Todo(Model):
    class StatusChoices(TextChoices):
        CLOSED = "closed", "Closed"
        IN_PROGRESS = "in_progress", "In Progress"
        NOT_STARTED = "not_started", "Not Started"

    created_at = DateTimeField(auto_now_add=True)
    description = TextField(blank=True, null=True)
    status = CharField(max_length=11, choices=StatusChoices, default=StatusChoices.IN_PROGRESS)
    title = CharField(max_length=127)
    updated_at = DateTimeField(auto_now=True)

    owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="todos")

    def __str__(self) -> str:
        return self.title
