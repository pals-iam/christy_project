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
    print('STEP 1')
    ip, is_routable = get_client_ip(request)
    print('STEP 2')
    if is_routable:
        print('STEP 3')

        API_KEY = os.environ['ipgeolocation_apiKey']
        url = f"https://api.ipgeolocation.io/v2/ipgeo?apiKey={API_KEY}&ip={ip}&fields=location"
        print('STEP 4')

        payload = {}
        headers = {}
        
        response = requests.request("GET", url, headers=headers, data={})
        print('STEP 5')
        location_data = json.loads(response.text)
        print('STEP 6')
        country_code2 = location_data['location']['country_code2']

        tld = '.com'
        print('STEP 7')

        if country_code2 in TLDS:
            tld = TLDS[country_code2]
        print('STEP 8')
    
        target_url = f'https://www.amazon{tld}/dp/{ASIN}'
        return HttpResponseRedirect(target_url)
    else:
        return HttpResponseRedirect(f'https://www.amazon.co.uk/dp/{ASIN}')

