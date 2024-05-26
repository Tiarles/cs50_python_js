from django.urls import path

from . import views

# app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entries, name="wiki_pages"),
    path("tmp", views.tmp, name="tmp"),
]
 