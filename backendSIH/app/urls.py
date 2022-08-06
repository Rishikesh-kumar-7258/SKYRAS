from django.urls import path, include
from .views import addScheme, index, signupForm, addDocument

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupForm, name="signup"),
    path('addScheme/', addScheme, name='addScheme'),
    path('addDocument/', addDocument, name='addDocument'),
]
