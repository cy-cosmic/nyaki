from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from adminapp.models import ForestRidgeHome, RStreetHome, FoodAndActivities


@login_required
# Create your views here.
def index(request):
    return render(request, "admin/index.html", locals())


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin")
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, "admin/login.html", locals())


@login_required
def forest_ridge(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        photo = ForestRidgeHome.objects.create(image=image)
        photo.save()
    photos = ForestRidgeHome.objects.all()
    return render(request, "admin/forest-ridge.html", locals())


@login_required
def rstreet(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        photo = RStreetHome.objects.create(image=image)
        photo.save()
    photos = RStreetHome.objects.all()
    return render(request, "admin/rstreet.html", locals())


@login_required
def activities(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        photo = FoodAndActivities.objects.create(image=image)
        photo.save()
    photos = FoodAndActivities.objects.all()
    return render(request, "admin/activities.html", locals())


@login_required
def delete_forest(request, id):
    if request.method == "POST":
        obj = ForestRidgeHome.objects.get(id=id)
        obj.delete()
        return JsonResponse({"success": True})


@login_required
def delete_rstreet(request, id):
    if request.method == "POST":
        obj = RStreetHome.objects.get(id=id)
        obj.delete()
        return JsonResponse({"success": True})


@login_required
def delete_activities(request, id):
    if request.method == "POST":
        obj = FoodAndActivities.objects.get(id=id)
        obj.delete()
        return JsonResponse({"success": True})
