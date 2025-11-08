from django.shortcuts import render
from .helpers import *

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def book(request):
    return render(request, 'website/book.html')

def contact(request):
    if request.method == 'POST':
        form = request.POST

        gmail_send_message(
                intent = 'contact_form_submission',
                user_name = form['name'],
                user_email = form['email'],
                user_subject = form['subject'],
                user_message = form['message']
            )
    return render(request, 'website/contact.html')

