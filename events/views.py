from http import HTTPStatus

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def index(request):
    return HttpResponse(status=HTTPStatus.OK, content_type='text',
                        content='Hello, Space Marine!')
