from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import EventLocation, Event, EventContainer
from copy import deepcopy

# event_admin_fieldsets = deepcopy(PageAdmin.fieldsets)
# event_admin_fieldsets[0][1]["fields"]

class EventLocationAdmin(admin.ModelAdmin):
	def in_menu(self):
		return 0

class EventAdmin (PageAdmin):
	fieldsets = (
		deepcopy(PageAdmin.fieldsets[0]),
		("Event details",{
			'fields': ('content', ('start_datetime', 'end_datetime'), 'event_location', 'speakers', 'rsvp')
		}),
		deepcopy(PageAdmin.fieldsets[1]),
	)

admin.site.register(EventLocation, EventLocationAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(EventContainer, PageAdmin)
