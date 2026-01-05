from django.db import models
from django.db.models import Q# Code written by Bauyrzhan Kappassov
from django.contrib.auth.models import User
from django.conf import settings# Code written by Bauyrzhan Kappassov
from django.db.models import QuerySet
# Code written by Bauyrzhan Kappassov


# Code written by Bauyrzhan Kappassov

class VideoQuerySet(models.QuerySet):
    # Code written by Bauyrzhan Kappassov
    def is_public(self):
        return self.filter(active=True)  # Code written by Bauyrzhan Kappassov

    # Code written by Bauyrzhan Kappassov
    def search(self, query=None, user=None):
        # Code written by Bauyrzhan Kappassov
        if query:# Code written by Bauyrzhan Kappassov
            lookup = Q(title__icontains=query) | Q(description__icontains=query)|Q(created_at__icontains=query)# Code written by Bauyrzhan Kappassov
        else:# Code written by Bauyrzhan Kappassov
            lookup = Q()  # Code written by Bauyrzhan Kappassov

        # Code written by Bauyrzhan Kappassov
        qs = self.is_public().filter(lookup)

        # Code written by Bauyrzhan Kappassov
        if user:# Code written by Bauyrzhan Kappassov
            qs = qs.filter(user=user)

        # Code written by Bauyrzhan Kappassov
        return qs.distinct()
# Bauyrzhan Kappassov

class VideoManager(models.Manager):# Code written by Bauyrzhan Kappassov
    def get_queryset(self, *args, **kwargs):
        return VideoQuerySet(self.model, using=self._db)

    # Code written by Bauyrzhan Kappassov
    def search(self, query, user=None):# Code written by Bauyrzhan Kappassov
        return self.get_queryset().search(query, user=user)

# Code written by Bauyrzhan Kappassov

class Video(models.Model):# Code written by Bauyrzhan Kappassov
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)# Code written by Bauyrzhan Kappassov
    title = models.CharField(max_length=200)  # Code written by Bauyrzhan Kappassov
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True) # # Code written by Bauyrzhan Kappassov
    created_at = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    # Code written by Bauyrzhan Kappassov
    objects = VideoManager()

    # Code written by Bauyrzhan Kappassov



    def __str__(self): # Code written by Bauyrzhan Kappassov
        return self.title# Code written by Bauyrzhan Kappassov

# Bauyrzhan Kappassov

