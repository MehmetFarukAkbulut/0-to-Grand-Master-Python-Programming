from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display= ('id','name','created_date')


# Register your models here.

admin.site.register(Movie, MovieAdmin)