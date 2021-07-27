from currency.models import ContactUs
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World")

def contact_us(request):
    contacts = ContactUs.objects.all()

    result = []
    for contact in contacts:
        result.append(
            f"id: {contact.id} name: {contact.email_from}  subject: {contact.subject}  message: {contact.message}</br>"
        )

    return HttpResponse(str(result))
