from django.urls import path, include
# Code written by Bauyrzhan Kappassov
from . import views

"""
 Author: Bauyrzhan Kappassov
 Handles video uploads for the app.
 """
urlpatterns=[
    path('',views.SearchListView.as_view(),name='search'), # Bauyrzhan Kappassov
    # Bauyrzhan Kappassov
]# Code written by Bauyrzhan Kappassov