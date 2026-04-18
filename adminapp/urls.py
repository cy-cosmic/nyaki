from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from adminapp import views

app_name = 'admin'
urlpatterns = [
    path("", views.index, name="admin"),
    path("forest-ridge/", views.forest_ridge, name="forest_ridge"),
    path("forest-ridge/delete/<int:id>/", views.delete_forest, name="delete_forest"),
    path("rstreet/", views.rstreet, name="rstreet"),
    path("rstreet/delete/<int:id>/", views.delete_rstreet, name="delete_rstreet"),
    path("activities/", views.activities, name="activities"),
    path("activities/delete/<int:id>/", views.delete_activities, name="delete_activities"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)