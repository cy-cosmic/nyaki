from django.urls import path

from nyakiapp import views

urlpatterns = [
    path("", views.index, name="index"),
]
