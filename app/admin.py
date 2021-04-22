from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('word',)


admin.site.register(Word, WordAdmin)

