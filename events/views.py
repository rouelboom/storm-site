from http import HTTPStatus

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import Event


def index(request):

    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


@login_required
def new_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.author = request.user
        new_event.save()
        print('form is valid')
        return redirect('events:index')
    return render(request, 'new_event.html', {'form': form})

@login_required
def registrate_to_event(requset, event_id):
    event = get_object_or_404(Event, id=event_id)
    if requset.user == event.author:
        print('man, you cant registrate to your event by yourself')
        return redirect('events:index')
    event.opponent = requset.user
    event.lobby_is_open = False
    event.save()
    print('you was registred')
    return redirect('events:index')
