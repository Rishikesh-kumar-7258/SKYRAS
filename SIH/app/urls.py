from django.urls import path
from .views import AboutUs, CompleteProfile, ContactUs, Profile, Schemes, SignUp, addDocument, deleteDocument, verifyDocument, viewDocument, HomePage, FogotPassword, Help, CreateScheme

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
    path('register', SignUp.as_view(), name="register"),
    path('forgotPassword/', FogotPassword.as_view(), name="forgotPassword"),
    path('completeProfile/', CompleteProfile.as_view(), name="completeProfile"),
    path('profile/', Profile.as_view(), name="profile"),

    # scheme related urls
    path('allSchemes/', Schemes.as_view(), name="schemes"),
    path('addScheme/', CreateScheme, name="addScheme"),

    # help related url
    path("help/", Help.as_view(), name="help"),

    # about us
    path("aboutUs/", AboutUs.as_view(), name="aboutUs"),

    # contactUs
    path("contactUs/", ContactUs.as_view(), name="contactUs"),


]
