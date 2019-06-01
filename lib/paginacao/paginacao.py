from django.conf import settings
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.utils.urls import remove_query_param, replace_query_param
from rest_framework.pagination import _get_displayed_page_numbers


class MyPagination(pagination.PageNumberPagination):
    def _get_page_links(self, page_numbers, current, url_func):
        page_links = []
        for index, page_number in enumerate(page_numbers):
            if page_number is None:
                page_link = {
                    'index': index,
                    'url': None,
                    'number': None,
                    'is_active': False
                }
            else:
                page_link = {
                    'index': index,
                    'url': url_func(page_number),
                    'number': page_number,
                    'is_active': (page_number == current),
                }
            page_links.append(page_link)
        return page_links

    def get_paginated_response(self, data):
        base_url = self.request.build_absolute_uri()

        def page_number_to_url(page_number):
            if page_number == 1:
                return remove_query_param(
                    base_url,
                    self.page_query_param
                )
            else:
                return replace_query_param(
                    base_url,
                    self.page_query_param, page_number
                )

        current = self.page.number
        total_pages = self.page.paginator.num_pages
        page_links = self._get_page_links(
            _get_displayed_page_numbers(current, total_pages),
            current, page_number_to_url
        )

        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'pages': page_links,
            'count': self.page.paginator.count,
            'total_pages': total_pages,
            'results': data
        })
