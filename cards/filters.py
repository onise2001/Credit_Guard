from rest_framework.filters import BaseFilterBackend


class CardFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        queryset = queryset.filter(user=request.user)
        return queryset