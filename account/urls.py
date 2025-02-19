from account.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'auth'

urlpatterns = [
    path('login/', userLogin, name="login"),
    path('logout/', userLogout, name='logout'),
    path('register/', userRegister, name="register"),

    # path('profile/', userProfile, name="profile"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)