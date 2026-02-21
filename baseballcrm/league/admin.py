from django.contrib import admin
from .models import Team, Player, Minor
from .models import Prospect,Gaa_Team, News, Conference
from .models import  NCAA_TEAM, NCAA_Player, Stock

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Minor)
admin.site.register(Prospect)
admin.site.register(Gaa_Team)
admin.site.register(News)
admin.site.register(Conference)
admin.site.register(NCAA_TEAM)
admin.site.register(NCAA_Player)
admin.site.register(Stock)


# Register your models here. News
