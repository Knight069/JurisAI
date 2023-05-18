from django.urls import include, path
from home.views import home , about, contact, features, pricing, waitlist, chatbot, chatAPI
from django.contrib import admin

urlpatterns = [
    path('home', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('features', features, name='features'),
    path('chatbot', chatbot, name='chatbot'),
    path('pricing', pricing, name='pricing'),
    path('waitlist', waitlist, name='waitlist'),
    path('api', chatAPI, name='chatAPI'),
]
