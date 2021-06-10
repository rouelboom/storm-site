from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_event/', views.new_event, name='new_event'),
    path('reg_to_event/<int:event_id>/', views.registrate_to_event,
         name='reg_to_event'),
    path('from_bot/', views.answer_to_telegram, name='from_bot'),
]
