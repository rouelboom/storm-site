from http import HTTPStatus
import datetime as dt

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import EventForm
from .models import Event


def index(request):

    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})


# @login_required
def new_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.author = request.user
        new_event.save()
        print('form is valid')
        return redirect('events:index')
    return render(request, 'new_event.html', {'form': form})


# @login_required
def registrate_to_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user == event.author:
        print('man, you cant registrate to your event by yourself')
        return redirect('events:index')
    event.opponent = request.user
    event.lobby_is_open = False
    event.save()
    print('you was registred')
    return redirect('events:index')


def answer_to_telegram(request):
    event = Event(title='Большой бабах', type='Warhammer40k', event_date=dt.datetime.now().isoformat())
    event.save()
    return HttpResponse('yo bitch')
