from django.shortcuts import render

from .forms import DocumentForm, ProfileForm, SchemeForm


def index(request):
    return render(request, 'index.html', {})


def addDocument(request):

    if request.method == "POST":
        documentForm = DocumentForm(request.POST, request.FILES)
        if documentForm.is_valid():
            documentForm.save()
            return render(request, 'addDocument.html', {
                'documentForm': documentForm
            })
    else:
        documentForm = DocumentForm()
        return render(request, 'addDocument.html', {
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
            'form': form
        })
