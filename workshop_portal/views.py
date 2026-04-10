# Django Imports
from django.shortcuts import redirect, render
from django.urls import reverse
from django.conf import settings

# Local Imports
from cms.models import Page


def index(request):
    """Serve the landing page for unauthenticated users,
       redirect authenticated users to their dashboard."""
    user = request.user
    if user.is_authenticated:
        return redirect(reverse("workshop_app:index"))
    return render(request, 'workshop_app/landing.html')


def landing_page(request):
    """Direct access to the landing page (always)."""
    return render(request, 'workshop_app/landing.html')
