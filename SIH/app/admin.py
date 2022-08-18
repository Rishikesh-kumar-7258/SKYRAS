from django.contrib import admin
from .models import Category, Document, Profile, Scheme

admin.site.register(Document)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Scheme)
