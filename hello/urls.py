from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("mahmoud", views.mahmoud, name="mahmoud"),
    path("hazem", views.hazem, name="hazem"),
]