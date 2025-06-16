from django.shortcuts import render
from .forms import JobApplicationForm
from .models import Form
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            available_date = form.cleaned_data["available_date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                available_date=available_date,
                                occupation=occupation)

            messages.success(request, "The form was submitted successfully!")

    return render(request, "index.html")
