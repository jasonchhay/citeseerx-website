import urllib
import json
 
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.utils.safestring import mark_safe

# Create your views here.
def data(request):
    return render(request, 'psuwebsite/data.html')

def software(request):
    return render(request, 'psuwebsite/software.html')
'''
def submit(request):
    sent = False
    form = None
    message = ''
    error = False
    #Add in implementation to prevent header injection in a future date

    if request.method == 'POST':
        #Create a contact form with the given data
        form = SubmitForm(request.POST)

        print("Form is valid: {}".format(form.is_valid()))
        if form.is_valid():
            #Stores the validated data of the form

            #Taken from:
            #https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html
            Begin reCAPTCHA validation
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
            End reCAPTCHA validation

            print(str(result))
            
            #If the user is able to successfully validate the captcha and their information is correct
            if result['success']:
                cd = form.cleaned_data
                url = cd['url']
                contact_email = cd['email']
                contact_name = '{} {}'.format(cd['first_name'], cd['last_name'])
                content = '{}\nEmail: {}'.format(cd['url'],contact_email)

                send_mail('CiteSeerX: New Document From {}'.format(contact_name), content, contact_email, ['jasonchhay@gmail.com'])
                message = 'URL successfully submitted.'
            #If the user refreshes the page after they already submitted a POST
            elif result['error-codes'] and result['error-codes'] == ['timeout-or-duplicate']:
                print("Timeout-or-duplicate")
                message=""
            #If the Captcha fails for whatever reason
            else:
                message = 'Invalid reCAPTCHA. Please try again.'
                error=True
        #If the email address or URL is invalid
        elif form.errors:
            try:
                if form.errors['email']:
                    print("Enter a valid email address")
                    message += 'Please enter a valid email address.<br>'
                    error=True
            except(KeyError):
                pass;

            try: 
                if form.errors['url']:
                    print("Enter a valid URL")
                    message += 'Please enter a valid URL.<br>'
                    error = True
            except(KeyError):
                pass;
            
        else:
            form = SubmitForm(request.GET)

    return render(request, 'psuwebsite/submit.html', {'form' : form, 'message' : mark_safe(message), 'error' : error})
'''