from django import forms
from .models import Challenge, Submission

class flagSubmitForm(forms.Form):
    flag = forms.CharField(label='Flag', max_length=100)
    challenge_id = forms.IntegerField(widget=forms.HiddenInput())