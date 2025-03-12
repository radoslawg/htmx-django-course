from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import ContactForm


# Create your views here.
@login_required
def index(request):
    contacts = request.user.contacts.all().order_by("-created_at")
    context = {"contacts": contacts, "form": ContactForm()}
    return render(request, "contacts.html", context)


@login_required
def search_contacts(request):
    import time

    time.sleep(2)
    query = request.GET.get("search", "")
    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    ).order_by("-created_at")
    context = {"contacts": contacts}
    return render(request, "partials/contact-list.html", context)
