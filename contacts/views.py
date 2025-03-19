from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_http_methods

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


@login_required
@require_http_methods(["POST"])
def create_contact(request):
    form = ContactForm(request.POST, initial={"user": request.user})
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        response = render(request, "partials/contact-row.html", {"contact": contact})
        response["HX-Trigger"] = "success"
        return response
    else:
        response = render(request, "partials/add-contact-modal.html", {"form": form})
        response["HX-Retarget"] = "#contact_modal"
        response["HX-Reswap"] = "outerHTML"
        response["HX-Trigger-After-Settle"] = "fail"
        return response
