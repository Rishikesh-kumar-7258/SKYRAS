from django.urls import path, include
from .views import addScheme, index, signupForm

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signupForm, name="signup"),
    path('/addScheme', addScheme, name='addScheme')
]
