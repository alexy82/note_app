from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from django.urls import reverse

from .models import Notes

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    user = request.user
    list_notes = Notes.objects.filter(user=user).order_by('-created_at')

    return render(request, 'Notes/index.html', {'list_notes': list_notes})


@login_required
def note_delete(request, note_id):
    user = request.user
    if Notes.objects.filter(user=user, pk=note_id).exists():
        note = Notes.objects.get(pk=note_id)
        note.delete()

    return JsonResponse()


@login_required
def note_update(request, note_id):
    user = request.user
    if Notes.objects.filter(user=user, pk=note_id).exists():
        note = Notes.objects.get(pk=note_id)
        note.content = request.POST['content']
        note.save()

    return JsonResponse()


@login_required
def note_create(request):
    user = request.user
    Notes.objects.create(user=user)
    return HttpResponseRedirect(reverse('notes:index'))
