from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from .models import Team, Record
from .serializers import TeamSerializer, RecordSerializer

# Create your views here.


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()


@api_view(['GET'])
def team_detail(request, name):
    team = get_object_or_404(Team, name=name)

    victory_record = Record.objects.filter(winner=team)
    victory_data = [{'winner': r.winner.name, 'loser': r.loser.name,
                     'winner_score': r.winner_score, 'loser_score': r.loser_score} for r in victory_record]
    
    defeat_record = Record.objects.filter(loser=team)
    defeat_data = [{'winner': r.winner.name, 'loser': r.loser.name,
                     'winner_score': r.winner_score, 'loser_score': r.loser_score} for r in defeat_record]
    
    data = {}
    data['victory'] = victory_data
    data['defeat'] = defeat_data
    return Response(data)
