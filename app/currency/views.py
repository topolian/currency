from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView,
    UpdateView
)


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


# def rate_list(request):
#     rates = Rate.objects.all()
#
#     context = {
#         'rate_list': rates,
#     }
#
#     return render(request, 'rate_list.html', context=context)

class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rate_details.html'

# def rate_create(request):
#     if request.GET:
#         form = RateForm(request.GET)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list')
#
#     else:
#         form = RateForm()
#     context = {
#         'form': form,
#     }
#     # breakpoint()
#     return render(request, 'rate_create.html', context=context)


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'

# def source_list(request):
#     sources = Source.objects.all()
#
#     context = {
#         'source_list': sources,
#     }
#
#     return render(request, 'source_list.html', context=context)


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'

# def source_create(request):
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list')
#     elif request.method == 'GET':
#         form = SourceForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'source_create.html', context=context)


class SourceDetailsView(DetailView):
    queryset = Source.objects.all()
    template_name = 'source_details.html'

# def source_details(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#     context = {
#         'object': source,
#     }
#     return render(request, 'source_details.html', context=context)


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'

# def source_update(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#
#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=source)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list')
#     elif request.method == 'GET':
#         form = SourceForm(instance=source)
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'source_update.html', context=context)


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'

# def source_delete(request, source_id):
#     source = get_object_or_404(Source, id=source_id)
#
#     if request.method == 'POST':
#         source.delete()
#         return HttpResponseRedirect('/source/list')
#
#     context = {
#         'object': source,
#     }
#     return render(request, 'source_delete.html', context=context)
