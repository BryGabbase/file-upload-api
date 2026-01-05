from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Code written by Bauyrzhan Kappassov
from .viewset import UploaderViewSet

# Code written by Bauyrzhan Kappassov
router = DefaultRouter()
router.register(r'video-up',UploaderViewSet, basename='video')  # Make sure this matches the viewset and the intended URL

# Code written by Bauyrzhan Kappassov
print(router.urls)
urlpatterns=router.urls# Code written by Bauyrzhan Kappassov






