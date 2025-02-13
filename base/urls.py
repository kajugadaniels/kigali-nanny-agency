from base.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('services', services, name="services"),
    path('jobs', getJobs, name="getJobs"),
    path('job/slug', showJob, name="showJob"),
    path('contact', contact, name="contact"),
    path('signup', Signup, name="signup"),
    path('login', Login, name="login"),
    path('dashboard', Dashboard, name="dashboard"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
