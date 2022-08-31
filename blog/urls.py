from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:id>/", views.blog_detail, name="dlog_detail")
]