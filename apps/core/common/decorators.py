import json
from functools import wraps

from django.http import HttpResponse, HttpResponseNotAllowed


def api_route(content_type="application/json", methods=None):
    def outer(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if methods and request.method not in methods:
                return HttpResponseNotAllowed(methods)

            response = func(request, *args, **kwargs)

            if isinstance(response, HttpResponseNotAllowed):
                return response

            if isinstance(response, (tuple, list)):
                response, status = response
            else:
                response = {}
                status = 200

            return HttpResponse(
                json.dumps(response), status=status, content_type=content_type
            )

        return wrapper

    return outer
