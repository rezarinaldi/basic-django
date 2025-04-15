from django.urls import path
from .views import index_view, profile_view

urlpatterns = [
    path("", index_view, name="index"),
    path("profile/", profile_view, name="profile")
]