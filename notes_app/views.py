from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# Create your views here.


def all_notes(request):
    #return HttpResponse('<h1>Welcome in Django</h1>')
    all_notes = Note.objects.all()
    context = {
        'all_notes' :all_notes ,
    }

    return render(request , 'notes.html' , context)


def detail(request , slug):

    note = Note.objects.get(slug = slug)
    context = {
        'note': note ,
    }

    return render (request , 'one_note.html' , context)

def note_add(request):
    if request.method == 'POST' :
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Notes Created Successfully.')
            return redirect('/notes')
    else:
        form = NoteForm()
    context = {
        'form' : form ,
    }

    return render(request , 'add.html' , context)



def edit(request , slug):
    note = get_object_or_404(Note , slug = slug)
    if request.method == 'POST':
        form = NoteForm(request.POST , instance = note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/notes')
    else:
        form = NoteForm(instance=note)
    context = {
        'form': form ,
    }

    return render(request , 'create.html' , context)
