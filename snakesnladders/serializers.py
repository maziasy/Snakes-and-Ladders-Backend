from rest_framework import serializers
from .models import savedGames 

class savedGamesSerializer(serializers.ModelSerializer):
	class Meta: 
		model = savedGames
		fields = ('user', 'date_saved', 'position', 'greenDict', 'redDict')