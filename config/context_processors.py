from django.conf import settings


def project_metadata(request):
    return {
        "PROJECT_NAME": settings.PROJECT_NAME,
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "PROJECT_DESCRIPTION": settings.PROJECT_DESCRIPTION,
    }