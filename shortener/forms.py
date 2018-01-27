from django import forms
from shortener.validators import validate_url

class SubmitForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url])