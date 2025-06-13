# accounts/urls.py
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", response_view, name="home"),
    path('ajax-response/', views.ajax_response_view, name='ajax_response'),
    # ajax test study reponse
    path("ajax-study/", ajax_study, name="ajax-study"),
    path("get-message/", get_message, name="get-message"),
    path("say-hello/", say_hello, name="say-hello"),
]