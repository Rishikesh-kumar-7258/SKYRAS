from django.contrib import admin
from .models import Document, Scheme, User

# Register your models here.
admin.site.register(Document)
admin.site.register(Scheme)
admin.site.register(User)