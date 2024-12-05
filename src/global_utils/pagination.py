from typing import (
    Any,
    TypeVar,
    cast,
)

from django.conf import settings
from django.db.models import Model
from django.db.models.query import QuerySet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


_MT = TypeVar("_MT", bound=Model)


class CustomLimitOffsetPagination(LimitOffsetPagination):
    # TODO: Consider removing `cast()` since `settings.PG_MAX_BIGINT` is guaranteed to exist and is `int`
    # (used for type checking)
    default_limit = cast(int, settings.PG_MAX_BIGINT)  # type: ignore[misc]

    def paginate_queryset(self, queryset: QuerySet[_MT], request: Request, view: APIView | None = None) -> list[_MT]:
        self.request = request

        # TODO: Consider removing `cast()` since `self.default_limit` is guaranteed to be `int`
        # (used for type checking)
        self.limit = cast(int, self.get_limit(request))
        self.count = self.get_count(queryset)
        self.offset = self.get_offset(request)

        self.results_count = len(results_list := list(queryset[self.offset : self.offset + self.limit]))

        return results_list

    def get_paginated_response(self, data: Any) -> Response:
        return Response(
            {
                "meta": {
                    "total_items_count_for_user": self.count,
                    "results_count": self.results_count,
                },
                "results": data,
            }
        )
