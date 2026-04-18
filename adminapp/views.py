from django.http import JsonResponse
from django.shortcuts import render

from adminapp.models import ForestRidgeHome, RStreetHome, FoodAndActivities


# Create your views here.
def index(request):
    return render(request, "admin/index.html", locals())


def forest_ridge(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        photo = ForestRidgeHome.objects.create(image=image)
        photo.save()
    photos = ForestRidgeHome.objects.all()
    return render(request, "admin/forest-ridge.html", locals())


def rstreet(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        photo = RStreetHome.objects.create(image=image)
        photo.save()
    photos = RStreetHome.objects.all()
    return render(request, "admin/rstreet.html", locals())


def activities(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        photo = FoodAndActivities.objects.create(image=image)
        photo.save()
    photos = FoodAndActivities.objects.all()
    return render(request, "admin/activities.html", locals())


def delete_forest(request, id):
    if request.method == "POST":
        obj = ForestRidgeHome.objects.get(id=id)
        obj.delete()
        return JsonResponse({"success": True})


def delete_rstreet(request, id):
    if request.method == "POST":
        obj = RStreetHome.objects.get(id=id)
        obj.delete()
        return JsonResponse({"success": True})


def delete_activities(request, id):
    if request.method == "POST":
        obj = FoodAndActivities.objects.get(id=id)
        obj.delete()
        return JsonResponse({"success": True})
