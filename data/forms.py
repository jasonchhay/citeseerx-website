from django import forms

class SubmitForm(forms.Form):
    url = forms.URLField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)

