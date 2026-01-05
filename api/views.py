#import json    # for converting json into python dictionary

# Code written by Bauyrzhan Kappassov
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
#from django.forms.models import model_to_dict # make this simple
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializer import VideoSerializer
from product.models import Video # red one ignor code works fine
from django.http import HttpResponse
from rest_framework import status
# Code written by Bauyrzhan Kappassov





# Code written by Bauyrzhan Kappassov
@api_view(['POST'])
def Welcome_to_Uploader(request): # Code written by Bauyrzhan Kappassov
    if request.method == 'POST':# Code written by Bauyrzhan Kappassov
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():# Code written by Bauyrzhan Kappassov
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
## Code written by Bauyrzhan Kappassov

#     if request.method == 'GET':# Code written by Bauyrzhan Kappassov
#         videos = Video.objects.all()
#         serializer = VideoSerializer(videos, many=True, context={'request': request})
#         return Response(serializer.data)
# Code written by Bauyrzhan Kappassov




