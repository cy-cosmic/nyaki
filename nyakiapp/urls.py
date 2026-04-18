from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from nyakiapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.about, name="about"),
    path("services", views.services, name="services"),
    path("gallery", views.gallery, name="gallery"),
    path("contact-us", views.contact, name="contact"),
    path("api/reviews/", views.google_reviews, name="google-reviews"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)