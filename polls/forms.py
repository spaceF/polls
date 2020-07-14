from django import forms

from .models import Persons


class VotesForm(forms.ModelForm):
    """Голоса"""
    class Meta:
        model = Persons
        fields = ("surname", "votes")

