from django.urls import path
from .views import ( UploaderCreate,UploaderList,UploaderDelete,UploaderDetail,UploaderUpdate) # Code written by Bauyrzhan Kappassov
# Code written by Bauyrzhan Kappassov

urlpatterns=[
# Code written by Bauyrzhan Kappassov
    path('', UploaderCreate.as_view(), name='video-create'),
    path('list/',UploaderList.as_view(),name='video-list'),
    path('view/<int:pk>/',UploaderDetail.as_view(), name='video-detail'),
    path('delete/<int:pk>/', UploaderDelete.as_view(), name='video-delete'),
    path('update/<int:pk>/',UploaderUpdate.as_view(), name='video-update'),

# Bauyrzhan Kappassov

]
# Code written by Bauyrzhan Kappassov