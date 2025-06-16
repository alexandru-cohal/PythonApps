from django.shortcuts import render
from .forms import JobApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


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

            message_body = (f"Thank you for your submission, {first_name}.\n"
                            f"Here are your data:\n"
                            f"\t{first_name}\n"
                            f"\t{last_name}\n"
                            f"\t{available_date}\n"
                            f"\t{occupation}.\n"
                            f"Thank you!")
            email_message = EmailMessage(subject="Form Submission Confirmation",
                                         body=message_body,
                                         to=[email])
            email_message.send()

            messages.success(request, "The form was submitted successfully!")

    return render(request, "index.html")

def about(request):
    return render(request, "about.html")