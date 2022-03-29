from unicodedata import category
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Scheme
from .serializers import UserSerializer, SchemeSerializer, StatisticsSerializer

# Create your views here.
@api_view(["GET"])
def index(request):
    overview = {
        "name": "backend",
        "version": "0.0.1",
        "description": "backend API",
        "author": "SKYRAS",
    }
    return Response(overview)

# api to register user
@api_view(["POST"])
def create_user(request):
    
    if request.method == "POST":
        # getting form data
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        middle_name = request.data['middle_name']
        phone_number = request.data['phone_number']
        address = request.data['address']
        city = request.data['city']
        state = request.data['state']
        pin_code = request.data['pin_code']
        district = request.data['district']
        aadhar_number = request.data['aadhar_number']
        gender = request.data['gender']
        dob = request.data['dob']
        cat = request.data['category']


        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.middle_name - middle_name
        user.phone_number = phone_number
        user.address = address
        user.city = city
        user.state = state
        user.pin_code = pin_code
        user.district = district
        user.aadhar_number = aadhar_number
        user.dob = dob
        user.category = cat

        user.save()
        return Response("User saved successfully")

    return Response(status=status.HTTP_400_BAD_REQUEST)


# api to login user
@api_view(["POST"])
def login_user(request):
    
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("User logged in successfully")
        else :
            return Response("Invalid credentials")

    return Response(status=status.HTTP_400_BAD_REQUEST)


# api to logout user
@api_view(["POST"])
def logout_user(request):
    
    if request.method == "POST":
        logout(request)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# api to get user details
@api_view(["GET"])
def get_user_details(request):

    current_user = request.user.id
    serializer = UserSerializer(current_user)
    
    return Response(serializer)

# api to get scheme details
@api_view(["GET"])
def get_scheme_details(request, scheme_id):
    
    scheme = Scheme.objects.get(id=scheme_id)
    serializer = SchemeSerializer(scheme)
    return Response(serializer)

# api to get all schemes names + stats
@api_view(["GET"])
def get_all_schemes(request):
    
    schemes = Scheme.objects.all()
    serializer = SchemeSerializer(schemes, many=True)
    return Response(serializer)