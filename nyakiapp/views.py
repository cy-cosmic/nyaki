import random

from django.http import JsonResponse
from django.shortcuts import render

from nyakiapp.services.google_places import get_place_details_cached


# Create your views here.
def index(request):
    # get cached google reviews
    data = get_place_details_cached()
    reviews = [
        {
            "author": r.get("author_name"),
            "rating": r.get("rating"),
            "text": r.get("text"),
            "time": r.get("time"),
        }
        for r in data.get("reviews", [])
    ]
    cleaned_reviews = [
        {
            "name": r.get("author_name"),
            "photo": r.get("profile_photo_url") or "/static/img/man-user-circle-icon.png",
            "text": r.get("text"),
        }
        for r in reviews
        if r.get("text")  # avoid empty reviews
    ]
    sample_reviews = random.sample(cleaned_reviews, k=min(5, len(cleaned_reviews)))
    return render(request, "index.html", locals())


def google_reviews(request):
    data = get_place_details_cached()

    reviews = [
        {
            "author": r.get("author_name"),
            "rating": r.get("rating"),
            "text": r.get("text"),
            "time": r.get("time"),
        }
        for r in data.get("reviews", [])
    ]

    return JsonResponse({
        "name": data.get("name"),
        "rating": data.get("rating"),
        "total_reviews": data.get("user_ratings_total"),
        "reviews": reviews,
    })


def about(request):
    return render(request, "about.html", locals())


def services(request):
    return render(request, "services.html", locals())


def contact(request):
    return render(request, "contact.html", locals())


def gallery(request):
    return render(request, "gallery.html", locals())
