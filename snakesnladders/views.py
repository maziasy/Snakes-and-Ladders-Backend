from django.shortcuts import render
from rest_framework import viewsets
from .serializers import savedGamesSerializer
from .models import savedGames 

class savedGamesView(viewsets.ModelViewSet):
	serializer_class = savedGamesSerializer
	queryset = savedGames.objects.all()
# Create your views here.
