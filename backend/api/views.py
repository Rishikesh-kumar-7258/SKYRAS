from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Scheme

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


        # user = User.objects.create_user(username, email, password)
        # user.first_name = first_name
        # user.last_name = last_name
        # user.middle_name - middle_name

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

    current_user = request.user.id
    user = User.objects.get(id=current_user)
    
    return Response(user)

# api to get scheme details
@api_view(["GET"])
def get_scheme_details(request, scheme_id):
    
    scheme = Scheme.objects.get(id=scheme_id)
    return Response(scheme)

# api to get all schemes names + stats
@api_view(["GET"])
def get_all_schemes(request):
    
    schemes = Scheme.objects.all()
    return Response(schemes)