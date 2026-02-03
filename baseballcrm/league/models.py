from django.db import models

# lets make a Player model

class Team(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.city} self.name"