from django.http import HttpResponse  # noqa
from django.shortcuts import render


def manage_user_list(request):
    return render(request, "hello.html")
