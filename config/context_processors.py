from django.conf import settings


def project_metadata(request):
    return {
        "PROJECT_NAME": getattr(settings, "PROJECT_NAME", "Django Project"),
        "PROJECT_TITLE": getattr(settings, "PROJECT_TITLE", "Django Project"),
        "PROJECT_DESCRIPTION": getattr(settings, "PROJECT_DESCRIPTION", "Django Project Description"),
        # "PROJECT_DOMAIN": getattr(settings, "PROJECT_DOMAIN", "https://example.com"),
    }