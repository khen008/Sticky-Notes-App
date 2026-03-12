from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display all notes.
    """
    notes = Note.objects.all()
    return render(request, 'stickynotesapp/note_list.html', {'notes': notes})


def note_create(request):
    """
    Create a new note.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'stickynotesapp/note_form.html', {'form': form})


def note_update(request, pk):
    """
    Update an existing note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'stickynotesapp/note_form.html', {'form': form})


def note_delete(request, pk):
    """
    Delete a note.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('note_list')

    return render(request, 'stickynotesapp/note_confirm_delete.html', {'note': note})