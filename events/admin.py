from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'pub_date', 'opponent', 'description')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Event, EventAdmin)
