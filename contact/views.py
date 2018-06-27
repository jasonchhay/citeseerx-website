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
    error = False
    #Add in implementation to prevent header injection in a future date

    if request.method == 'POST':
        #Create a contact form with the given data
        form = ContactForm(request.POST)

        print("Form is valid: {}".format(form.is_valid()))
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

            print(str(result))
            
            #If the user is able to successfully validate the captcha and their information is correct
            if result['success']:
                cd = form.cleaned_data
                contact_name = "{} {}".format(cd['first_name'], cd['last_name'])
                contact_email = cd['email']
                contact_subject = 'CiteSeerX: Message from {}: {}'.format(contact_name,cd['subject'])
                content = '{}\nEmail: {}'.format(cd['content'],contact_email)

                send_mail(contact_subject, content, contact_email, ['jasonchhay@gmail.com'])
                message = 'E-mail sent successfully.'
            #If the user refreshes the page after they already submitted a POST
            elif result['error-codes'] and result['error-codes'] == ['timeout-or-duplicate']:
                print("Timeout-or-duplicate")
                message=""
            #If the Captcha fails for whatever reason
            else:
                message = 'Invalid reCAPTCHA. Please try again.'
                error=True
        #If the email address is invalid
        elif form.errors and form.errors['email']:
            print("Enter a valid email address")
            message = 'Please enter a valid email address.'
            error=True
            
    else:
        form = ContactForm(request.GET)

    return render(request, 'psuwebsite/contact.html', {'form' : form, 'message' : message, 'error' : error})