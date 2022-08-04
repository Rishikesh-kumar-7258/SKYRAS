from django.shortcuts import render

from .forms import DocumentForm, ProfileForm, SchemeForm


def index(request):
    documentForm = DocumentForm()
    return render(request, 'index.html', {
        'form': documentForm
    })


def signupForm(request):

    if request.method == "POST":
        pass
    else:

        form = ProfileForm()
        return render(request, 'signupform.html', {'form': form})

def addScheme(request):

    if request.method == "POST":
        pass
    else:
        form = SchemeForm()
        return render(request, 'addScheme.html', {
            'form' : form
        })