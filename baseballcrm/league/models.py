from django.db import models

# lets make a Player model

class Team(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.city}"
    
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
    at_bats = models.PositiveIntegerField(default=0)
    hits = models.PositiveIntegerField(default=0)
    def batting_average(self):
        if self.at_bats == 0:
            return 0.00
        return round(self.hits / self.at_bats, 3)

    position = models.CharField(max_length=2,
                                choices=POSITIONS)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null = True,
        blank=True,
        related_name="players"
    )

    def __str__(self):
        return f"{self.name}"
    

class Minor(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.city}"
    
class Prospect(models.Model):
    name = models.CharField(max_length=25)
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
    position = models.CharField(max_length=2,
                                choices=POSITIONS)
    def __str__(self):
        return f"{self.name} {self.position}"
    


class Gaa_Team(models.Model):
    name = models.CharField(max_length=25)
    rating = models.IntegerField(default=50)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"
    


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Conference(models.Model):
    conference_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.conference_name
    
class NCAA_TEAM(models.Model):
    team_name = models.CharField(max_length=100)
    conference_name = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        null = True,
        blank=True,
        related_name="conference_assigned"
    )
    def __str__(self):
        return self.team_name

class NCAA_Player(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    GP = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    GS = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TOT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    AVG = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FGM = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FGA = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FG_PERCENT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Three_PT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Three_PTA = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Three_PT_PERCENT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FTA = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    FT_PERCENT = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    PTS = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    AVG = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.first} {self.last}"
    
class Stock(models.Model):
    company = models.CharField(max_length=100)
    total_shares = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.company}"

class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    

    
