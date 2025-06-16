from django.shortcuts import render
from .forms import JobApplicationForm


def index(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            available_date = form.cleaned_data["available_date"]
            occupation = form.cleaned_data["occupation"]
            
    return render(request, "index.html")
