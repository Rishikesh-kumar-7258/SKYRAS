from django.urls import path
from .views import CompleteProfile, Profile, SignUp, addDocument, deleteDocument, verifyDocument, viewDocument, HomePage, SignIn, FogotPassword

urlpatterns = [
    path('', HomePage.as_view(), name="homepage"),

    # document related urls
    path('viewDocuments', viewDocument.as_view(), name='viewDocuments'),
    path('addDocument/', addDocument.as_view(), name='addDocument'),
    path('verifyDocument/<int:pk>',
         verifyDocument.as_view(), name='verifyDocument'),
    path('deleteDocument/<int:pk>',
         deleteDocument.as_view(), name='deleteDocument'),

    # user related urls
    path('signIn/', SignIn.as_view(), name='signIn'),
    path('register', SignUp.as_view(), name="register"),
    path('forgotPassword/', FogotPassword.as_view(), name="forgotPassword"),
    path('completeProfile/', CompleteProfile.as_view(), name="completeProfile"),
    path('profile', Profile.as_view(), name="profile")
]
