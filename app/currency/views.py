from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


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

    context = {
        'rate_list': rates,
    }

    return render(request, 'rate_list.html', context=context)


def rate_create(request):
    if request.GET:
        form = RateForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list')

    else:
        form = RateForm()
    context = {
        'form': form,
    }
    # breakpoint()
    return render(request, 'rate_create.html', context=context)


def source_list(request):
    sources = Source.objects.all()

    context = {
        'source_list': sources,
    }

    return render(request, 'source_list.html', context=context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form,
    }
    return render(request, 'source_create.html', context=context)


def source_details(request, source_id):
    source = get_object_or_404(Source, id=source_id)
    context = {
        'object': source,
    }
    return render(request, 'source_details.html', context=context)


def source_update(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form,
    }
    return render(request, 'source_update.html', context=context)


def source_delete(request, source_id):
    source = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list')

    context = {
        'object': source,
    }
    return render(request, 'source_delete.html', context=context)