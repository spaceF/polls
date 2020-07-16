from django import forms


class AddVoteForm(forms.Form):
    """Форма голосования"""
    person = forms.CharField(max_length=200)
