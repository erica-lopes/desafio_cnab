from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="cnab_txt"),
    path("upload/list/", views.rendering),
]
