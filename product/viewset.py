from rest_framework import viewsets
from .models import Video
from .serializer import VideoSerializer # Bauyrzhan Kappassov
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
# Bauyrzhan Kappassov


# Code written by Bauyrzhan Kappassov
class UploaderViewSet(viewsets.ModelViewSet): # Code written by Bauyrzhan Kappassov

    queryset = Video.objects.all() # Bauyrzhan Kappassov
    serializer_class = VideoSerializer
    lookup_field = 'pk'

    # Code written by Bauyrzhan Kappassov
    def retrieve(self, request, *args, **kwargs): # Code written by Bauyrzhan Kappassov
        instance = self.get_object() # Bauyrzhan Kappassov
        serializer = self.get_serializer(instance)

        return Response(  # Bauyrzhan Kappassov
            { # Bauyrzhan Kappassov
                "video": serializer.data,
                # Bauyrzhan Kappassov
                "Go To List": reverse("video-list", request=request),
            },

            status=status.HTTP_200_OK)
# Code written by Bauyrzhan Kappassov


