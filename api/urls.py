from django.urls import path
from.import views# Code written by Bauyrzhan Kappassov
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)
# Bauyrzhan Kappassov


# Code written by Bauyrzhan Kappassov
urlpatterns=[# Code written by Bauyrzhan Kappassov
    path('',views.Welcome_to_Uploader,name='home'),
    path('auth/',obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]

# Code written by Bauyrzhan Kappassov


