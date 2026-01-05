from rest_framework.response import Response
# Bauyrzhan Kappassov
from .models import Video
from rest_framework import status
from rest_framework.reverse import reverse
from .serializer import  VideoSerializer
from rest_framework.decorators import api_view
# Bauyrzhan Kappassov
from rest_framework import viewsets,mixins,generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from permissions import IsDocPermission
# from rest_framework.permissions import IsAuthenticated
# Bauyrzhan Kappassov




# Bauyrzhan Kappassov

class UploaderList(generics.ListAPIView): # Bauyrzhan Kappassov
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

 # Bauyrzhan Kappassov


# Bauyrzhan Kappassov
class UploaderCreate(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def create(self, request, *args, **kwargs): # Bauyrzhan Kappassov
        super().create(request, *args, **kwargs)

        return Response({ # Bauyrzhan Kappassov
            "Message": "Thank you! Your data has been saved successfully.",
            "Go To List": reverse('video-list', request=request)
        }, status=status.HTTP_201_CREATED)




class UploaderUpdate(generics.UpdateAPIView): # Bauyrzhan Kappassov
    queryset = Video.objects.all()
    serializer_class = VideoSerializer # Bauyrzhan Kappassov
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs): # Bauyrzhan Kappassov
        serializer = self.get_serializer( # Bauyrzhan Kappassov
            self.get_object(), data=request.data, partial=True
        ) # Bauyrzhan Kappassov
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) # Bauyrzhan Kappassov

        return Response({ # Bauyrzhan Kappassov
            "message": "Your data has been updated successfully.",
            "uploader": serializer.data, # Bauyrzhan Kappassov
            "Go To List": reverse("video-list", request=request)
        }, status=status.HTTP_200_OK) # Bauyrzhan Kappassov



class UploaderDelete(generics.DestroyAPIView): # Bauyrzhan Kappassov
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'pk' # Bauyrzhan Kappassov

    def destroy(self, request, *args, **kwargs): # Bauyrzhan Kappassov
        instance = self.get_object() # Bauyrzhan Kappassov
        self.perform_destroy(instance)

        return Response(
            { # Bauyrzhan Kappassov
                "message": "Your data has been deleted successfully.",
                "go_to_list": reverse("video-list", request=request),
            }, # Bauyrzhan Kappassov
            status=status.HTTP_200_OK) # Bauyrzhan Kappassov


#Bauyrzhan Kappassov
class UploaderDetail(generics.RetrieveAPIView): # Bauyrzhan Kappassov
    queryset = Video.objects.all()
    serializer_class = VideoSerializer # Bauyrzhan Kappassov
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # Bauyrzhan Kappassov
        serializer = self.get_serializer(instance)

        return Response( # Bauyrzhan Kappassov
            {
                "video": serializer.data, # Bauyrzhan Kappassov

                "Go To List": reverse("video-list", request=request), # Bauyrzhan Kappassov
                },

            status=status.HTTP_200_OK # Bauyrzhan Kappassov
        )

#Bauyrzhan Kappassov



