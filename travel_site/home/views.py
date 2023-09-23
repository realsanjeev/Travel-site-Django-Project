import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from home.models import Contact
from home.forms import ContactForm

def display_in_console(statement: str) -> None:
    '''
    Print in console
    '''
    print("-" * 100)
    print(statement)
    print("-" * 100)

@csrf_protect
def contact(request):
    context = {}
    feedback_records = Contact.objects.all()
    print(len(feedback_records))

    try:
        context["records"] = feedback_records.reverse()
    except Exception as err:
        display_in_console(f"Exception occured: {err}\nfeedback records: {type(feedback_records)}")
        context["records"] = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context["form"] = form
            context["message"] = "Feedback is successfully registered."
            return redirect("contact")
    else:
        form = ContactForm()
    context["form"] = form
    return render(request, "contact.html", context)


def places(request):
    return render(request, "places.html")

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
