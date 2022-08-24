from django.core.mail import (EmailMessage, EmailMultiAlternatives)
from django.conf import settings
from django.template.loader import get_template


class EmailMessage(forms):

    def send_mail(self, request):
        
        email = EmailMessage(
                subject = 'New Contact Form Entry',
                body = "",
                from_email = 'no-reply@example.com',
                reply_to = ['no-reply@example.com'],
                cc = [],
                bcc = [],
                to = [],
                attachments = [],
                headers = {},
            )
        email.content_subtype = 'plain'
        email.send()
        email.send(fail_silently=True)

    def send_email_as_html(self, request):
        data={'Name':"My Name", "Title":"Ecommerce"}
        template = get_template('chapter_7/emails/new_contact_form_entry.html')
        context = {'data': data} #you can call each data in the html template
        msg_body = template.render(context)

        # msg_body = '<b>Hello World</b>'
        email = EmailMultiAlternatives(
            subject = 'New Contact Form Entry',
            body = msg_body,
            from_email = 'no-reply@example.com',
            reply_to = ['no-reply@example.com'],
            cc = [],
            bcc = [],
            to = [],
            attachments = [],
            headers = {},
        )
        email.content_subtype = 'html'
        email.attach_alternative(
            'Hello World',
            'text/plain'
        )
        email.send()
        email.send(fail_silently=True)

    def send_email_with_attachments(self, request):
        msg_body = '<b>Hello World</b>'
        email = EmailMultiAlternatives(
            subject = 'New Contact Form Entry',
            body = msg_body,
            from_email = 'no-reply@example.com',
            reply_to = ['no-reply@example.com'],
            cc = [],
            bcc = [],
            to = [],
            attachments = [],
            headers = {},
        )
        email.content_subtype = 'html'
        email.attach_alternative(
            'Hello World',
            'text/plain'
        )
        email.attach_file(settings.STATIC_ROOT + '/chapter_7/pdf/example.pdf')
        email.send()
        email.send(fail_silently=True)
