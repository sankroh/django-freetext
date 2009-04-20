from django.contrib import admin
from free_text.models import FreeText
 
class FreeTextAdmin(admin.ModelAdmin):
    ordering = ['title',]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'header', 'content')
    search_fields = ('title', 'slug', 'header', 'content')

admin.site.register(FreeText, FreeTextAdmin)