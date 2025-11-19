from django.shortcuts import render
from ipware import get_client_ip
from .helpers import *
from .context_processors import global_variables

import requests, json, re

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

def amazon_redirect(request):
    ASIN = 'B0FYZCF7F4'    

    ip, is_routable = get_client_ip(request)
    if is_routable:

        API_KEY = os.environ['ipgeolocation_apiKey']
        url = f"https://api.ipgeolocation.io/v2/ipgeo?apiKey={API_KEY}&ip={ip}&fields=location"

        payload = {}
        headers = {}
        
        response = requests.request("GET", url, headers=headers, data={})
        location_data = json.loads(response.text)
        country_code2 = location_data['location']['country_code2']

        tld = '.com'

        if country_code2 in TLDS:
            tld = TLDS[country_code2]
    
        target_url = f'https://www.amazon{tld}/dp/{ASIN}'
        return HttpResponseRedirect(target_url)
    else:
        return HttpResponseRedirect(f'https://www.amazon.co.uk/dp/{ASIN}')

