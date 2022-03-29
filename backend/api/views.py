from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from .models import User

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
        address = request.data['address']
        city = request.data['city']
        state = request.data['state']
        pin_code = request.data['pin_code']
        district = request.data['district']
        adhaar_number = request.data['adhaar_number']
        phone_number = request.data['phone_number']
        gender = request.data['gender']
        dob = request.data['dob']
        category = request.data['category']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        middle_name = request.data['middle_name']


        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.middle_name = middle_name
        user.email = email
        user.password = password
        user.address = address 
        user.city = city
        user.state = state
        user.pin_code = pin_code
        user.district = district
        user.adhaar_number = adhaar_number
        user.phone_number = phone_number
        user.gender = gender
        user.dob = dob
        user.category = category
        





        # todo : Add different fields from the user form like user.middle_name= middle_name

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
    # todo : get user details
    pass

# api to get scheme details
@api_view(["GET"])
def get_scheme_details(request):
    # todo : get scheme details
    pass

# api to get all schemes names + stats
@api_view(["GET"])
def get_all_schemes(request):
    # todo : get all schemes names + stats
    pass