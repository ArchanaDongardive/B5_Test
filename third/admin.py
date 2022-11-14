from django.contrib import admin

# Register your models here.

from .models import Booklet

admin.site.register([Booklet])
