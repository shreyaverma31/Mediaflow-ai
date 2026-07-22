from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("upload/", views.upload_video),
    path("jobs/", views.jobs),
    path("stats/", views.stats),
]