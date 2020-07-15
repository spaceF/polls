from django import forms

from .models import Persons


class VotesForm(forms.ModelForm):
    """Форма голосования"""
    class Meta:
        model = Persons
        fields = '__all__'


