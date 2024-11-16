from django.contrib import admin
from .models import Meal, Rating




class MealAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description'] 


class RatingAdmin(admin.ModelAdmin):
    list_display = ['meal', 'user', 'stars']
    list_filter = ['meal', 'user']



admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)