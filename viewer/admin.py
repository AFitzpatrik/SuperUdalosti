from django.contrib import admin

from viewer.models import Country, City, Location, Event, Comment

# Register your models here.


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Comment)