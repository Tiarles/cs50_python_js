from django.urls import path

from . import views

# app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),

    path("new", views.new_page, name="new_page"),
    path("random", views.random_page, name="random_page"),
    path("edit/<str:title>", views.edit_page, name="edit_page"),

    path("<str:title>", views.entries, name="wiki_pages"),
]
