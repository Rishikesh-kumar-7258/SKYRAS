from django.contrib import admin
from .models import Document, Profile, Scheme, SchemeRegistration, SchemeTracking

admin.site.register(Document)
admin.site.register(Profile)
admin.site.register(Scheme)
admin.site.register(SchemeRegistration)
admin.site.register(SchemeTracking)
