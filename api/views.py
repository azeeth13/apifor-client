from django.shortcuts import render
# from rest_framework import generics
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.forms import model_to_dict
from allauth.account.views import SignupView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view



@api_view(['GET'])
def UserSignUp(request):
    user=request.user
    serializer=UserSerializer(user)
    return Response(serializer.data)



def IndexPage(request):
    return render(request,'index.html')


class CustomSignUser(SignupView):
    def form_valid(self,form):
        user=form.save(self.request)
        Token.objects.get_or_create(user=user)
        return super().form_valid(form)
    
class UserSignUp(APIView):
    '''Users Api'''
    def get(self,request):
        users=User.objects.all().values()
        return Response({'users':users})
    
    def post(self,request):
        username=request.data['username']
        email=request.data['email']
        password1=request.data['password']
        password2=request.data['password2']

        if password1==password2:
            new_user=User.objects.create_user(
                username=username,
                email=email,
                password=password1  
            )
            return Response({'users':model_to_dict(new_user)})
