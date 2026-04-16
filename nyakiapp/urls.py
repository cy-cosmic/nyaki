from django.urls import path

from nyakiapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.about, name="about"),
    path("services", views.services, name="services"),
    path("gallery", views.gallery, name="gallery"),
    path("contact-us", views.contact, name="contact"),
]
