from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html", {
        "page_title": "About",
        "page_description": "Learn about the Django, HTMX, Alpine.js, and Tailwind CSS starter.",
    })