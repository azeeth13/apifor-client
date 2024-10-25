from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']    


