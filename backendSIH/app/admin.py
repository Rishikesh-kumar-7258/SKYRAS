from django.contrib import admin
from .models import Document, Profile, Scheme

# Register your models here.
admin.site.register(Document)
admin.site.register(Scheme)
admin.site.register(Profile)