from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # todo : Add differnet paths form the view.py sectons
]
