from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("user/", views.get_current_user),
]
