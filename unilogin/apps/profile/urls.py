from django.urls import path

from . import views

app_name = "profile"

urlpatterns = [
    path("", views.profile_view, name="profile"),
    path("settings/<int:pk>", views.UpdateUserView.as_view(), name="settings"),
]
