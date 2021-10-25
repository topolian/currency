from currency.views import (
    ContactUsCreateView,
    RateCreateView, RateDetailView, RateListView,
    SourceCreateView, SourceDeleteView, SourceDetailsView,
    SourceListView, SourceUpdateView, contact_us
)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('contact-us/', contact_us, name='contact-us'),
    path('contact-us/create/', ContactUsCreateView.as_view(), name='contact-us-create'),
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailsView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
]
