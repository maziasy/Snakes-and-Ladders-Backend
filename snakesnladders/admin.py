from django.contrib import admin
from .models import savedGames

class savedGamesAdmin(admin.ModelAdmin):
	list_display = ('user', 'date_saved', 'position', 'greenDict', 'redDict')

admin.site.register(savedGames, savedGamesAdmin)

# Register your models here.
