from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginator(PageNumberPagination):
    page_size = 100
    page_query_param = 'page_size'
    max_page_size = 100


