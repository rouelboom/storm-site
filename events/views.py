from http import HTTPStatus

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import EventForm


def index(request):
    return HttpResponse(status=HTTPStatus.OK, content_type='text',
                        content='Hello, Space Marine!')

@login_required
def new_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.author = request.user
        new_event.save()
        return redirect('events:index')
    return render(request, 'new_event.html', {'form': form})
