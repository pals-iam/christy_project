"""Gmail API Dependencies"""
from google.oauth2 import service_account
from googleapiclient.discovery import build
import base64
from email.message import EmailMessage
from googleapiclient.errors import HttpError
import google.auth  
import json, os, requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


HELP_DESK_EMAIL = 'christiana@christianacatherine.co.uk'
NO_REPLY_EMAIL = 'christiana@christianacatherine.co.uk'
COMPANY_NAME = 'Christiana Catherine'

def gmail_send_message(**kwargs):
    

    """Gmail API"""
    service_account_info = json.loads(os.environ['SERVICE_ACCOUNT_KEY'])
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    
    # SERVICE_ACCOUNT_FILE = 'service_account_emailSystem.json'
    # credentials = service_account.Credentials.from_service_account_file(
    #     filename=SERVICE_ACCOUNT_FILE,
    #     scopes=['https://mail.google.com/'],
    #     subject='christiana@christianacatherine.co.uk'
    # )

    credentials = credentials.with_scopes(['https://mail.google.com/'])

    # Define contect for contact form submission and automatic message reply
    if not kwargs['intent'] == 'membership_request':
        context = {
                'user_name': kwargs['user_name'],
                'user_email': kwargs['user_email'],
                'user_subject': kwargs['user_subject'],
                'user_message': kwargs['user_message'],
                'company_name': COMPANY_NAME
            }

    """ HELPDESK EMAIL MESSAGING ITSELF TO GIVE NOTIFICATION OF CONTACT FORM SUBMISSION """
    if kwargs['intent'] == 'contact_form_submission':
        
        credentials = credentials.with_subject(HELP_DESK_EMAIL)
        
        try:
            service = build('gmail', 'v1', credentials=credentials)
            message = MIMEMultipart('alternative')
            message['To'] = HELP_DESK_EMAIL
            message['From'] = HELP_DESK_EMAIL
            message['Subject'] = 'Internal Notification'
            message['List-Unsubscribe'] = '<https://www.christianacatherine.co.uk/unsubscribe>'
            message['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
            
            template_name = 'mailing_system/internal_notification.html'

            html_content = render_to_string(template_name, context)
            message.attach(MIMEText(html_content, 'html'))

            # Send Email 
            delete=False  
            send_mail(service, message, delete)

        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None

        kwargs.pop('intent', None)

        gmail_send_message(
            intent='contact_form_reply', 
            **kwargs
            )
        
        return True  #JsonResponse(send_message, safe=False)
        
    """ AUTOMATIC REPLY TO CONTACT FORM SUBMISSIONS """    
    if kwargs['intent'] == 'contact_form_reply':

        credentials = credentials.with_subject(HELP_DESK_EMAIL)

        try:
            service = build('gmail', 'v1', credentials=credentials)
            message = MIMEMultipart('alternative')
            message['To'] = kwargs['user_email']
            message['From'] = HELP_DESK_EMAIL
            message['Subject'] = kwargs['user_subject']
            message['List-Unsubscribe'] = '<https://www.christianacatherine.co.uk/unsubscribe>'
            message['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'

            template_name = 'mailing_system/automatic_reply.html'

            html_content = render_to_string(template_name, context)
            message.attach(MIMEText(html_content, 'html'))

            # Send Email   
            delete=True
            send_mail(service, message, delete)

        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None

        return True  #JsonResponse(send_message, safe=False)
    
    # """ AUTOMATIC REPLY TO MEMBERSHIP REQUESTS """
    # if kwargs['intent'] == 'membership_request':

    #     credentials = credentials.with_subject(NO_REPLY_EMAIL)

    #     try:
    #         service = build('gmail', 'v1', credentials=credentials)
    #         message = MIMEMultipart('alternative')
    #         message['To'] = kwargs['user_email']
    #         message['From'] = NO_REPLY_EMAIL
    #         message['Subject'] = 'Membership Application Received'
    #         message['List-Unsubscribe'] = '<https://www.antiguabarbudapensioners.org/unsubscribe>'
    #         message['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'

    #         template_name = 'mailing_system/membership_email.html'
    #         kwargs['company_name'] = COMPANY_NAME

    #         html_content = render_to_string(template_name, kwargs)
    #         message.attach(MIMEText(html_content, 'html'))

    #         # Send Email   
    #         send_mail(service, message)

    #     except HttpError as error:
    #         print(F'An error occurred: {error}')
    #         send_message = None

    #     return True  #JsonResponse(send_message, safe=False)
        

def send_mail(service, message, delete):
    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
        .decode()

    create_message = {
        'raw': encoded_message
    }
    # pylint: disable=E1101
    send_message = (service.users().messages().send(userId="me", body=create_message).execute())
    message_id = send_message['id']
    print(F'Message Id: {message_id}')

    if delete:
        delete_message = service.users().messages().trash(userId="me", id=message_id).execute()
        print(delete_message)

    return


TLDS = {
    # 'US': '.com',
    'GB': '.co.uk',
    'DE': '.de',
    'AT': '.de',
    'FR': '.fr',
    'ES': '.es',
    'IT': '.it',
    'NL': '.nl',
    'PL': '.pl',
    'SE': '.se',
    'BE': '.com.be',
    'IE': '.ie',
    'JP': '.co.jp',
    'CA': '.ca',
    'AU': '.com.au'
}
