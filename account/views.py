from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from account.serializers import UserProfileSerializer, UserRegistrationSerializer,UserLoginSerializer
from account.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from account.renderers import UserRenderer
from django.contrib.auth import authenticate
# from .utils import verification_email

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegisterationView(APIView):
    renderer_classes=[UserRenderer]
    serializer_class=UserRegistrationSerializer
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            token = get_tokens_for_user(user=user)
            # verification_email(user.email,user.name)
            return Response({"token":token,"msg":"User Registered Succesfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    serializer_class=UserLoginSerializer
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user) 
                return Response({"token":token,"msg":"User Found"},status=status.HTTP_200_OK)
            else:
                #serializer use nahi kar rahe isliye custom handle karna pad raha hai..warna as above handle ho jata
                return Response({'errors':{'non_field_errors':["Email or password is not valid"]}},status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    serializer_class=UserLoginSerializer
    
    def get(self,request,format=None):
        print("Request",request.user)
        serializer= UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)