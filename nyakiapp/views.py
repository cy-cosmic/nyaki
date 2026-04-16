from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())


def about(request):
    return render(request, "about.html", locals())


def services(request):
    return render(request, "services.html", locals())

def contact(request):
    return render(request, "contact.html", locals())


def gallery(request):
    return render(request, "gallery.html", locals())