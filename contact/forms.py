from django import forms

# Create your models here.
class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=250)
    content = forms.CharField(required=True, widget=forms.Textarea)