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
            json_response = {}
            status = 200

            if isinstance(response, HttpResponseNotAllowed):
                return response

            if isinstance(response, (tuple, list)):
                json_response, status = response
            elif isinstance(response, dict):
                json_response = response

            return HttpResponse(
                json.dumps(json_response), status=status, content_type=content_type
            )

        return wrapper

    return outer
