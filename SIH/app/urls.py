from django.urls import path
from .views import AboutUs, ChangePassword, CompleteProfile, ContactUs, Login, ProfileView, SchemeRegistrationView, Schemes, SignUp, addDocument, deleteDocument, verifyDocument, viewDocument, HomePage, Help, CreateScheme, EditProfileImage, TrackScheme, OneScheme

urlpatterns = [
    path('', HomePage, name="homepage"),

    # document related urls
    path('viewDocuments/<int:pk>', viewDocument.as_view(), name='viewDocument'),
    path('addDocument/', addDocument.as_view(), name='addDocument'),
    path('verifyDocument/<int:pk>',
         verifyDocument.as_view(), name='verifyDocument'),
    path('deleteDocument/<int:pk>',
         deleteDocument.as_view(), name='deleteDocument'),

    # user related urls
    path('register', SignUp.as_view(), name="register"),
    path('login/', Login, name="login"),
    path('completeProfile/', CompleteProfile, name="completeProfile"),
    path('profile/', ProfileView, name="profile"),
    path('editProfilePic/<int:pk>',
         EditProfileImage, name="editProfilePic"),
    path('changePassword/', ChangePassword, name="changePassword"),

    # scheme related urls
    path('allSchemes/', Schemes, name="schemes"),
    path('addScheme/', CreateScheme, name="addScheme"),
    path('schemeRegistration/<int:pk>',
         SchemeRegistrationView, name="schemeRegistration"),
    path('trackScheme/<int:pk>', TrackScheme, name="trackScheme"),
    path('scheme/<int:pk>', OneScheme.as_view(), name="scheme"),

    # help url
    path("help/", Help.as_view(), name="help"),

    # about us
    path("aboutUs/", AboutUs.as_view(), name="aboutUs"),

    # contactUs
    path("contactUs/", ContactUs.as_view(), name="contactUs"),


]
