# Code written by Bauyrzhan Kappassov
from rest_framework import serializers
from.models import Video # Bauyrzhan Kappassov
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator



# Code written by Bauyrzhan Kappassov

def validate_title(value): # Code written by Bauyrzhan Kappassov
    qs =Video.objects.filter (title__iexact=value) # Code written by Bauyrzhan Kappassov
    if qs.exists():  # Bauyrzhan Kappassov
        raise ValidationError(f'{value} already exists.Create a new one!')
    forbidden_words = ["stupid","dumb","ugly","loser","fat","hate","kill","dead","retarded","weak","idiot","crazy"]
    if value.lower() in forbidden_words: # Bauyrzhan Kappassov
        raise ValidationError("You cannot use  this word")
    elif value.upper() in forbidden_words:
        raise ValidationError("This title contains forbidden words!")# Code written by Bauyrzhan Kappassov
    else: # Code written by Bauyrzhan Kappassov
        return value
# Code written by Bauyrzhan Kappassov

# Code written by Bauyrzhan Kappassov
def validate_description(value): # Bauyrzhan Kappassov
    queryset=Video.objects.filter( description__iexact=value)
    if queryset.exists(): # Bauyrzhan Kappassov
        raise  ValidationError(f'this content is already exist ')
    else: # Bauyrzhan Kappassov
        return value
# Code written by Bauyrzhan Kappassov









def validate_title_no_word(value): #  # Bauyrzhan Kappassov
    if'hello'in value.lower(): # Bauyrzhan Kappassovv
        raise serializers.ValidationError(f'this word is not allowed')
    else: # Bauyrzhan Kappassov
        return value # Bauyrzhan Kappassov


# we added ( lookup='iexact')-> coz of dividedly of user data

unique_product_title=UniqueValidator(queryset=Video.objects.all(),lookup="iexact") # Bauyrzhan Kappassov

