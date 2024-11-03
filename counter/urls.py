from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.count_word_text, name="get_len"),
]