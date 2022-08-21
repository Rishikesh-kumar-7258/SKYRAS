from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Document, Scheme, Profile, SchemeRegistration, SchemeTracking
from .forms import CompleteProfileForm, CreateDocumentForm, EditProfilePictureForm, LoginForm, RegisterForm, CreateSchemeForm, SchemeRegistrationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.utils import timezone
# from sms import send_sms


################################# Utility Variables ################################################
TODAY = timezone.now()

################################# Utility Functions ################################################


def getLatestSchemes(count):
    s = Scheme.objects.all().order_by("startDate").values()[:count]
    print(s)
    return s


def aboutToLast(count):
    s = Scheme.objects.filter(endDate__range=(
        TODAY, TODAY+timezone.timedelta(days=30))).order_by("endDate").values()[:count]

    return s


def isSuperUser(user):
    return user.is_superuser


#################################### Normal Views ################################################
def HomePage(request):
    return render(request, "home.html", {"schemes": getLatestSchemes(3), "aboutToLast": aboutToLast(3)})


class Help(TemplateView):
    template_name = "help.html"


class AboutUs(TemplateView):
    template_name = "aboutUs.html"


class ContactUs(TemplateView):
    template_name = "contactUs.html"


################################# Document related views ################################################
class viewDocument(LoginRequiredMixin, DetailView):
    model = Document
    template_name = "document/viewDocument.html"


class addDocument(LoginRequiredMixin, CreateView):
    model = Document
    form_class = CreateDocumentForm
    template_name = "document/addDocument.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.user = self.request.user
        app_model.save()
        return super().form_valid(form)


class verifyDocument(LoginRequiredMixin, UpdateView):
    model = Document
    template_name = "document/verifyDocument.html"
    fields = ['verified']
    success_url = '/'


class deleteDocument(LoginRequiredMixin, DeleteView):
    model = Document
    template_name = "document/deleteDocument.html"
    success_url = '/'


######################## User Registration and Login related views #################################
class SignUp(CreateView):
    model = User
    form_class = RegisterForm
    template_name: str = "users/register.html"
    success_url = reverse_lazy('login')


@login_required
def ChangePassword(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect("login")
        else:
            messages.error(request, "Please correct the error below.")
            return HttpResponse(form.errors)
    else:
        form = PasswordChangeForm(request.user)
        return render(request, "users/changePassword.html", {"form": form})


@login_required
def ProfileView(request):
    documents = Document.objects.filter(user=request.user.id)
    return render(request, "users/profile.html", {"user": request.user, "documents": documents})

# to create profile of the user


@login_required
def CompleteProfile(request):

    if request.method == "POST":
        form = CompleteProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            return HttpResponse("Invalid details")
    else:
        form = CompleteProfileForm()

    return render(request, "users/completeProfile.html", {"form": form})


@login_required
def EditProfileImage(request, pk):

    if request.method == "POST":
        profile = Profile.objects.filter(id=pk).first()
        print(profile.state)
        profile.img = request.FILES['img']
        profile.save()
        return redirect("profile")
    else:
        form = EditProfilePictureForm()
        return render(request, "users/editPic.html", {"form": form})


def Login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return HttpResponse("Invalid credentials")

    form = LoginForm()
    return render(request, "users/login.html", {"form": form})


################################# Scheme related views ################################################
class Schemes(ListView):
    model = Scheme
    template_name = "schemes/scheme.html"
    queryset = Scheme.objects.all()


@user_passes_test(isSuperUser)
def CreateScheme(request):

    if request.method == "POST":
        form = CreateSchemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # sending mails whenever a scheme is created
            superusers_emails = User.objects.filter(
                is_superuser=True).values_list('email')
            # user_number = Profile.objects.all().values_list('phone_number')
            receivers = [email[0] for email in list(superusers_emails)]
            # phone_reciever = [phone[0] for phone in list(user_number)]
            subject = "New scheme created"
            body = "A new scheme is created please visit the website to know more"
            send_mail(subject, body, 'SKYRAS', receivers, fail_silently=False)
            # send_sms(body, "SKYRAS", phone_reciever, fail_silently=False)
            return redirect('homepage')
        else:
            return HttpResponse(form.errors)
    else:
        form = CreateSchemeForm()
    return render(request, "schemes/create.html", {"form": form})


@login_required
def SchemeRegistrationView(request, pk):
    if request.method == "POST":
        form = SchemeRegistrationForm(request.POST, request.FILES)
        tracker = SchemeTracking.objects.create(
            user=request.user, scheme=Scheme.objects.get(pk=pk), registered=True)

        if form.is_valid():

            tracker.save()

            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.scheme = Scheme.objects.get(pk=pk)
            form_obj.created_data = TODAY
            form_obj.save()
            return redirect("trackScheme", pk=pk)
        else:
            return HttpResponse(form.errors)
    else:
        exists = False
        if SchemeRegistration.objects.filter(scheme=pk, user=request.user.id).exists():
            exists = True
        form = SchemeRegistrationForm()
        return render(request, "schemes/register.html", {"form": form, "pk": pk, "exists": exists})


@login_required
def TrackScheme(request, pk):
    tracker = SchemeTracking.objects.filter(
        scheme=pk, user=request.user.id).first()
    return render(request, "schemes/tracker_scheme.html", {"tracker": tracker})


class OneScheme(DetailView):
    model = Scheme
    template_name = "schemes/single_scheme.html"
