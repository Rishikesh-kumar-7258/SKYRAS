from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Document
from .forms import PostForm


class viewDocument(ListView):
    model = Document
    template_name = "document/viewDocuments.html"
    queryset = Document.objects.all()


class addDocument(CreateView):
    model = Document
    form_class = PostForm
    template_name = "document/addDocument.html"
    success_url = '/'


class verifyDocument(UpdateView):
    model = Document
    template_name = "document/verifyDocument.html"
    fields = ['verified']
    success_url = '/'

class deleteDocument(DeleteView):
    model = Document
    template_name = "document/deleteDocument.html"
    success_url = '/'