from django.contrib import admin
from .models import User, Scheme, Statistics

# Register your models here.
admin.site.register(User)
admin.site.register(Scheme)
admin.site.register(Statistics)