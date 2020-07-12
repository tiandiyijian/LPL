from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=5)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    opponents = models.ManyToManyField("self", through='Record', through_fields=('winner', 'loser'))

    def __str__(self):
        return self.name

class Record(models.Model):
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='game_winner')
    loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='game_loser')
    winner_score = models.SmallIntegerField(default=2)
    loser_score = models.SmallIntegerField(default=0)
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.winner.name} {self.winner_score}:{self.loser_score} {self.loser.name}'