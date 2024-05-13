from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("css", views.css, name="css"),
    # path("django", views.django, name="django"),
    path("tmp", views.tmp, name="tmp"),
    path("<str:title>", views.entries, name="wiki_pages"),
]
 