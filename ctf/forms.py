# ctf/forms.py
from django import forms

class FlagSubmitForm(forms.Form):
    flag = forms.CharField(
        label='Flag',
        max_length=100,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "CSEC{...}", "rows": 2}
        ),
    )
    challenge_id = forms.IntegerField(widget=forms.HiddenInput())
