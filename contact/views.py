import urllib
import json
 
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def contact(request):
    sent = False
    form = None
    message = ''
    #Add in implementation to prevent header injection in a future date

    if request.method == 'POST':
        #Create a contact form with the given data
        form = ContactForm(request.POST)

        if form.is_valid():
            #Stores the validated data of the form

            #Taken from:
            #https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': '6Ldjh2AUAAAAADQ6e09oK6XSE_C18qgbwy0AhnQZ',
                'response': request.POST.get('g-recaptcha-response')
            }

            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                cd = form.cleaned_data
                contact_name = cd['name']
                contact_email = cd['email']
                contact_subject = 'CiteSeerX: Message from {}: {}'.format(contact_name,cd['subject'])
                content = '{}\nEmail: {}'.format(cd['content'],contact_email)

                send_mail(contact_subject, content, contact_email, ['jasonchhay@gmail.com'])
                message = 'E-mail sent successfully.'
            else:
                message = 'Invalid reCAPTCHA. Please try again.'

    else:
        form = ContactForm(request.GET)

    return render(request, 'psuwebsite/contact.html', {'form' : form, 'message' : message})