from rest_framework import generics
from product.models import Video # Bauyrzhan Kappassov
from product.serializer import VideoSerializer


# Code written by Bauyrzhan Kappassov

class SearchListView(generics.ListAPIView): # Bauyrzhan Kappassov
    queryset =Video.objects.all()
    serializer_class = VideoSerializer # Bauyrzhan Kappassov
    #  # Bauyrzhan Kappassov

    def get_queryset(self,*args,**kwargs): # Code written by Bauyrzhan Kappassov
        qs=super().get_queryset(*args, **kwargs)# Code written by Bauyrzhan Kappassov

        q=self.request.GET.get('q')  # Code written by Bauyrzhan Kappassov
        results = qs.search(q) #  # Bauyrzhan Kappassov
        if q is None: # Bauyrzhan Kappassov
            user=None # Code written by Bauyrzhan Kappassov
            if self.request.user.is_authenticated: #  # Bauyrzhan Kappassov
                user=self.request.user # # Bauyrzhan Kappassov
            results = qs.search(q, user=user) #  # Bauyrzhan Kappassov
        return results #  # Bauyrzhan Kappassov

 # Bauyrzhan Kappassov