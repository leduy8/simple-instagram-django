from django.urls import path

from apps.core.views.user_views import manage_user_list

urlpatterns = [path("users/", manage_user_list)]
