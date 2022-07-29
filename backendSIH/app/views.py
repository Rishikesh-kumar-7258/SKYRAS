from django.shortcuts import render

from .forms import DocumentForm


def index(request):
    documentForm = DocumentForm()
    return render(request, 'index.html', {
        'form': documentForm
    })
