from django.urls import path

from . import views

# app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("new_page", views.new_page, name="new_page"),
    path("random_page", views.random_page, name="random_page"),
    path("<str:title>", views.entries, name="wiki_pages"),
]
