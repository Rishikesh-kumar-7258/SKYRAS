from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

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