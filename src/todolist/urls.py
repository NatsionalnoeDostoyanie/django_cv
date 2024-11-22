from django.conf import settings
from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter

from todolist.views import TodoViewSet


router = DefaultRouter()
router.register("", TodoViewSet, basename=settings.PG_DATABASE_NAME)  # type: ignore[misc]

urlpatterns = (path("", include(router.urls)),)
