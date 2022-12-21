from django.contrib import admin
from .models import Campaign, Character, Map, Location, Note

class mapAdmin(admin.ModelAdmin):
	list_display = ["map_title", "map_image"]

admin.site.register(Campaign)
admin.site.register(Character)
admin.site.register(Map, mapAdmin)
admin.site.register(Location)
admin.site.register(Note)
