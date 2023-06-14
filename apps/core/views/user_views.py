from apps.core.common.decorators import api_route


@api_route(methods=["GET"])
def manage_user_list(request):
    data = {"ok?": "ok!", "really?": "yes!"}
    return data, 200
