from rest_framework import serializers
from .models import Video
# Code written by Bauyrzhan Kappassov
from django.utils import timezone
from .validators import validate_title, validate_description, validate_title_no_word
from rest_framework.validators import UniqueValidator

# Code written by Bauyrzhan Kappassov
class VideoSerializer(serializers.ModelSerializer):
    queryset = Video.objects.all()


    comment = serializers.CharField(write_only=True,required=False)

    title = serializers.CharField(validators=[UniqueValidator(queryset=Video.objects.all())])
    description = serializers.CharField(validators=[validate_description])
    # comment = serializers.CharField(validators=[validate_title_no_word])
    #
    # update_url = serializers.HyperlinkedIdentityField(view_name='video-update',lookup_field='pk')  # this can be a lot not only one like navbar in drf
    # delete_url= serializers.HyperlinkedIdentityField(view_name='video-delete', lookup_field='pk')
    detail_url = serializers.HyperlinkedIdentityField(view_name='video-detail', lookup_field='pk')

    created_at = serializers.DateTimeField(format="%d-%m-%y ", default_timezone=timezone.get_current_timezone(), read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%y %H:%M:%S", default_timezone=timezone.get_current_timezone(),read_only=True)

    # date_of_creation = serializers.DateTimeField(source="created_at", read_only=True, format="%d-%m-%Y ")
    # Code written by Bauyrzhan Kappassov
    # attach_video_document = serializers.FileField(source='video_file')
    # time = serializers.DateTimeField(default=timezone.now)
#Bauyrzhan Kappassov
    class Meta:
        model = Video # Code written by Bauyrzhan Kappassov
        fields = [
            "id",
            "detail_url",
            "title",
            "description",
            "video_file",
            "comment",
            "time",
            "created_at",
            "updated_at",
            "public",
            # Code written by Bauyrzhan Kappassov
        ]
    def create(self, validated_data): # Code written by Bauyrzhan Kappassov
        comment = validated_data.pop('comment', None)  # remove it safely
        video = Video.objects.create(**validated_data)
        if comment:
            # Code written by Bauyrzhan Kappassov
            pass
        # Code written by Bauyrzhan Kappassov
        return video





