from django.http import HttpResponse  # noqa
from django.shortcuts import render


def say_hello(request):
    return render(request, "hello.html")
