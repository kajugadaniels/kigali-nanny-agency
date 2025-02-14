from base.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', home, name="home"),

    path('dashboard/', dashboard, name="dashboard"),

    path('job-listings/', getJobListings, name="getJobListings"),
    path('job-listing/add/', addJobListing, name="addJobListing"),
    path('job-listing/edit/<slug:slug>/', editJobListing, name="editJobListing"),
    path('job-listing/delete/<slug:slug>/', deleteJobListing, name="deleteJobListing"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)