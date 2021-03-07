from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

EVENT_TYPE_LIST = [('Warhammer40k', 'WH40K'),
                   ('SAGA', 'SAGA'),
                   ('Mallefaux', 'Mallefaux')]


class Event(models.Model):
    title = models.CharField('Название события', max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author',
                               verbose_name='Автор события',
                               help_text='Автор события')
    type = models.CharField('Тип события', max_length=50,
                            choices=EVENT_TYPE_LIST)
    pub_date = models.DateTimeField('Время создания события', auto_now_add=True)
    event_date = models.DateTimeField('Время проведения события',)
    opponent = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 related_name='opponent',
                                 verbose_name='Текущий опонент',
                                 help_text='Текущий опонент',
                                 blank=True,
                                 null=True)
    description = models.CharField('Описание события', max_length=500)
