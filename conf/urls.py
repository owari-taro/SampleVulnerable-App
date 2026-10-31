from django.contrib import admin
from django.urls import path

from api.api import api
from notes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("search/", views.search),
    path("hello/", views.hello),
    path("read/", views.read_file),
    path("ping/", views.ping),
    path("fetch/", views.fetch),
    path("yaml/", views.load_yaml),
    path("redirect/", views.go),
    path("notes/<int:note_id>/", views.note_detail),
]
