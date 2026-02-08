
from django import forms
from .models import Player
class PlayerStatForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["at_bats", "hits"]
        