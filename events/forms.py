from django import forms
from django.forms import Textarea

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'type', 'event_date', 'description')

        widgets = {'title': Textarea(attrs={'placeholder':
                                            'Введите название события',
                                            }),
                   'description': Textarea(attrs={'placeholder':
                                                  'Опишите условия/ограничения',
                                                  })}
