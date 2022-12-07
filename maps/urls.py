from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
	# Home Page
	path('', views.index, name='index'),
	# Page to show links to all maps
	path('maps/', views.maps, name = 'maps'),
	# Page to display a single map
	path('maps/<int:map_id>/', views.map, name='map'),
	# Page for adding a new map
	path('maps/new_map/', views.new_map, name='new_map'),
	# Page to display a single location, and all notes about it
	# Also includes a form to add new notes
	path('locations/<int:location_id>/', views.location, name='location'),
	# Page for adding a new location
	path('maps/<int:map_id>/new_location', views.new_location, name='new_location'),
]