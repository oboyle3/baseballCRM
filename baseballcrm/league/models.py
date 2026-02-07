from django.db import models

# lets make a Player model

class Team(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.city} self.name"
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    POSITIONS = [
        ("P", "Pitcher"),
        ("C", "Catcher"),
        ("1B", "First Base"),
        ("2B", "Second Base"),
        ("3B", "Third Base"),
        ("SS", "Shortstop"),
        ("LF", "Left Field"),
        ("CF", "Center Field"),
        ("RF", "Right Field"),
        ("DH", "Designated Hitter"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    position = models.CharField(max_length=2,
                                choices=POSITIONS)
    def __str__(self):
        return f"{self.name}"