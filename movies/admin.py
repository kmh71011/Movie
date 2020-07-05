from django.contrib import admin
from .models import Movie, Information

class InformationInline(admin.TabularInline):
    model = Information
    extra = 2

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [('Movie Statement', {'fields': ['movie_title', 'image', 'date']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']})]
    inlines = [InformationInline]
    list_display = ('movie_title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['movie_title']

admin.site.register(Movie)
admin.site.register(Information)
