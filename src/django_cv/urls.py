from django.contrib import admin
from django.urls import (
    include,
    path,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = (
    path("admin/", admin.site.urls),
    path("api/v1/todolist/", include("todolist.urls")),
    path("api/v1/token/", TokenObtainPairView.as_view()),
    path("api/v1/token/refresh/", TokenRefreshView.as_view()),
)
