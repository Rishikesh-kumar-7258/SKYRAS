from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Document, Scheme, Profile, SchemeRegistration, SchemeTracking, UserVerification
from .forms import CompleteProfileForm, CreateDocumentForm, EditProfilePictureForm, LoginForm, RegisterForm, CreateSchemeForm, SchemeRegistrationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.utils import timezone
from sms import send_sms
from django.conf import settings
import uuid

################################# Utility Variables ################################################
TODAY = timezone.now()

################################# Utility Functions ################################################


def getLatestSchemes(count):
    s = Scheme.objects.all().order_by("startDate").values()[:count]
    return s


def aboutToLast(count):
    s = Scheme.objects.filter(endDate__range=(
        TODAY, TODAY+timezone.timedelta(days=30))).order_by("endDate").values()[:count]

    return s


def get_details(pk):
    """ gets details of a particular scheme """
    details = {
        "total_registered": SchemeRegistration.objects.filter(scheme=pk).count(),
        "total_benefitted": SchemeTracking.objects.filter(scheme=pk, benefitted=True).count()
    }
    return details


def isSuperUser(user):
    return user.is_superuser


def send_email_token(email, token):
    try:
        subject = "Your account needs to be verified"
        message = f"Congratulations Use, you have successfullly reistered in Jan Swayam Kalyan Portal. Now, get all updates about schemes best suited for you. Click on the link to verify the email http://localhost:8000/verify/{token}/"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        return False
    return True


def send_sms_token(phone, token):
    try:
        subject = "Your account needs to be verified"
        message = f"Congratulations Use, you have successfullly reistered in Jan Swayam Kalyan Portal. Now, get all updates about schemes best suited for you. Click on the link to verify the email http://localhost:8000/verify/{token}/"
        recipient_list = [phone, ]
        send_sms(message, "SKYRAS", recipient_list, fail_silently=False)
    except Exception as e:
        return False
    return True

#################################### Normal Views ################################################


def HomePage(request):

    total_users = User.objects.all().count()
    total_schemes = Scheme.objects.all().count()
    total_benefitted = SchemeTracking.objects.filter(benefitted=True).count()

    dict = {
        "schemes": list(getLatestSchemes(6)),
        "aboutToLast": list(aboutToLast(3)),
        "total_user": total_users,
        "total_schemes": total_schemes,
        "total_benifitted": total_benefitted
    }
    return render(request, "home.html", dict)


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
# class SignUp(CreateView):
#     model = User
#     form_class = RegisterForm
#     template_name: str = "users/register.html"
#     success_url = reverse_lazy('login')


def SignUp(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        username = request.POST.get("username")

        if form.is_valid:
            form.save()

            verfication_obj = UserVerification.objects.create(
                user=User.objects.get(username=username),
                email_token=str(uuid.uuid4())
            )

            send_email_token(request.POST.get("email"),
                             verfication_obj.email_token)
            return redirect("login")

    else:
        form = RegisterForm()

        return render(request, "users/register.html", {"form": form})


def Verify(request, token):
    try:
        obj = UserVerification.objects.get(email_token=token)
        obj.is_verified = True
        obj.save()

        return HttpResponse("your account has been verified")
    except Exception as e:
        return HttpResponse("Invalid token")


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


@login_required
def CompleteProfile(request):

    if request.method == "POST":
        form = CompleteProfileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
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
# class Schemes(ListView):
#     model = Scheme
#     template_name = "schemes/scheme.html"
#     queryset = Scheme.objects.all()

def Schemes(request):

    if request.method == "GET":
        data = Scheme.objects.all()

        search = request.GET.get("search")
        if search:
            data = data.filter(name__icontains=search)

        recent = request.GET.get("recent")
        if recent and recent == "on":
            data = data.filter(endDate__range=(
                TODAY-timezone.timedelta(days=30), TODAY)).order_by("endDate")

        department = request.GET.get("department")
        if department and recent == "on":
            data = data.filter(department=department)

        sorted = request.GET.get("sorted")
        if sorted and sorted == "on":
            data = data.order_by("name")

        return render(request, "schemes/scheme.html", {"object_list": data})


@user_passes_test(isSuperUser)
def CreateScheme(request):

    if request.method == "POST":
        form = CreateSchemeForm(request.POST, request.FILES)
        department = request.POST.get("department")
        if form.is_valid():
            form.save()
            # sending mails whenever a scheme is created
            superusers_emails = User.objects.all().values_list('email')
            user_number = Profile.objects.all().values_list('phone_number')
            receivers = [email[0] for email in list(superusers_emails)]
            phone_reciever = [phone[0] for phone in list(user_number)]
            subject = "New scheme created"
            body = f"Dear User, a new scheme has been launched by {department}. For more information visit the website http://localhost:8000/schemes"
            send_mail(subject, body, 'SKYRAS', receivers, fail_silently=False)
            send_sms(body, "SKYRAS", phone_reciever, fail_silently=False)
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
        document_list = Scheme.objects.get(
            pk=pk).documents_required
        document_list = document_list.split(",")
        present_documents = Document.objects.filter(user=request.user)

        print(document_list, present_documents)

        for document in present_documents:
            for doc2 in document_list:
                if document.name.lower() == doc2.lower():
                    document_list.remove(doc2)

        return render(request, "schemes/register.html",
                      {
                          "form": form,
                          "pk": pk,
                          "exists": exists,
                          "documents_required": document_list,
                          "document_required_count": len(document_list)
                      })


@login_required
def TrackScheme(request, pk):
    tracker = SchemeTracking.objects.filter(
        scheme=pk, user=request.user.id).first()
    return render(request, "schemes/tracker_scheme.html", {"tracker": tracker})


@login_required
def SearchRegisteredScheme(request):

    object_list = SchemeRegistration.objects.filter(user=request.user)
    print(object_list)
    return render(request, "schemes/search_registered.html", {"object_list": object_list})


def OneScheme(request, pk):

    dict = get_details(pk)
    dict["object"] = Scheme.objects.get(pk=pk)
    return render(request, "schemes/single_scheme.html", dict)


def SchemesForYou(request):

    age = TODAY.year - request.user.profile.dob.year - \
        ((TODAY.month, TODAY.day) <
         (request.user.profile.dob.month, request.user.profile.dob.day))
    object_list = Scheme.objects.filter(
        age_min__lte=age)
    object_list = Scheme.objects.filter(
        age_max__gte=age)

    object_list = object_list.filter(
        income_min__lte=request.user.profile.income)
    object_list = object_list.filter(
        income_max__gte=request.user.profile.income)

    object_list = object_list.filter()
    print(age)
    return render(request, "schemes/forYou.html", {"object_list": object_list})
