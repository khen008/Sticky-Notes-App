from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Note model.
    """

    list_display = ('title', 'created_at')


admin.site.register(Note, NoteAdmin)