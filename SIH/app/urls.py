from django.urls import path
from .views import AboutUs, CompleteProfile, ContactUs, Login, ProfileView, Schemes, SignUp, addDocument, deleteDocument, verifyDocument, viewDocument, HomePage, FogotPassword, Help, CreateScheme, EditProfileImage

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
    path('login/', Login, name="login"),
    path('completeProfile/', CompleteProfile, name="completeProfile"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('editProfilePic/<int:pk>',
         EditProfileImage, name="editProfilePic"),

    # scheme related urls
    path('allSchemes/', Schemes.as_view(), name="schemes"),
    path('addScheme/', CreateScheme, name="addScheme"),

    # help url
    path("help/", Help.as_view(), name="help"),

    # about us
    path("aboutUs/", AboutUs.as_view(), name="aboutUs"),

    # contactUs
    path("contactUs/", ContactUs.as_view(), name="contactUs"),


]
