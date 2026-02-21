
from django import forms
from .models import Player, Stock


#goal = make a model form for the below model

# class Stock(models.Model):
#     company = models.CharField(max_length=100)
#     total_shares = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     def __str__(self):
#         return f"{self.company}"


class Stockform(forms.ModelForm): # forms.ModelForm is used to automatatacally connect to a model
    class Meta:
        model = Stock
        fields = ['company', 'total_shares', 'price']