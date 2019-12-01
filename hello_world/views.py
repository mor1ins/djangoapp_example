from django.shortcuts import render
from django.http import HttpResponse


def get_pages(count : int) -> str:
    return ' '.join([f'<a href="/page{i}">page{i}</a>' for i in range(1, count + 1)])


def page_one(request):
    return HttpResponse(f'Hello, world. I am page one!<br/><br/>{get_pages(2)}')


def page_two(request):
    return HttpResponse(f'I am page two. And I love you.<br/><br/>{get_pages(2)}')


def index(request):
    return HttpResponse(get_pages(2))
