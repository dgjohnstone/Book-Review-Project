"""belt_review_project URL Configuration

project urls
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.login_app.urls')),
    url(r'^main/', include('apps.book_app.urls')),
]
