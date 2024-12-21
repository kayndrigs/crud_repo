# notes_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    form = NoteForm()
    return render(request, 'notes_app/note_list.html', {'notes': notes, 'form': form})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return JsonResponse({
                'id': note.id,
                'title': note.title,
                'content': note.content,
                'created_at': note.created_at.strftime('%B %d, %Y, %I:%M %p')
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return JsonResponse({
                'title': note.title,
                'content': note.content,
            })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_note(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return JsonResponse({'message': 'Note deleted successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)