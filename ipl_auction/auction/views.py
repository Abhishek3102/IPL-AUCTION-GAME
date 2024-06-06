from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=['post'])
    def bid(self, request):
        team_id = request.data.get('team_id')
        player_id = request.data.get('player_id')
        amount = request.data.get('amount')

        team = Team.objects.get(id=team_id)
        player = Player.objects.get(id=player_id)

        if team.budget >= float(amount):
            player.team = team
            team.budget -= float(amount)
            player.save()
            team.save()
            return Response({'status': 'success', 'message': 'Player bought successfully.'})
        else:
            return Response({'status': 'failure', 'message': 'Not enough budget.'})

