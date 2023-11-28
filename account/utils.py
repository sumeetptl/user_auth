from django.core.mail import send_mail
from django.conf import settings

import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        reciepents = [data['to_email']]
        send_mail(
    		subject=data['email_subject'],
    		message=data['email_body'],
    		from_email=settings.EMAIL_HOST_USER,
    		recipient_list=reciepents)