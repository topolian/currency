from django.shortcuts import render

from currency.models import ContactUs, Rate

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def contact_us(request):
    contacts = ContactUs.objects.all()

    # result = []
    # for contact in contacts:
    #     result.append(
    #         f"id: {contact.id} "
    #         f"name: {contact.email_from}  "
    #         f"subject: {contact.subject}  "
    #         f"message: {contact.message}</br>"
    #     )

    context = {
        'contact_us': contacts,
    }

    return render(request, 'contact_us.html', context=context)


def rate_list(request):
    rates = Rate.objects.all()
    #
    # result = []
    # for rate in rates:
    #     result.append(
    #         f"Id: {rate.id} Sale: {rate.sale} Buy: {rate.buy} Created: {rate.created} Source: {rate.source} Type: {rate.type}</br>"
    #     )

    context = {
        'rate_list': rates,
    }

    return render(request, 'rate_list.html', context=context)
