from django import forms


class JobApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    available_date = forms.DateField()
    occupation = forms.CharField(max_length=80)