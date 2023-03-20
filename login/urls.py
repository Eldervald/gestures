from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    #path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('loginWithVideo/', LoginUserWithVideo.as_view(), name='loginWithVideo'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('loginWithVideo/classification', classification, name='classification'),



]