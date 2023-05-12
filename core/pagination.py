from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'limit'


class BasicPagination(PageNumberPagination):
    page_size = 100

