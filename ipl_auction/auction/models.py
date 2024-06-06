from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    expertise_level = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
