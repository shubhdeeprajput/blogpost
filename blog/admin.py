from django.contrib import admin

# Register your models here.
from .models import Profile,Pst

admin.site.register(Profile)
admin.site.register(Pst)