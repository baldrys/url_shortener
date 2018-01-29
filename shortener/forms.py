from django import forms
from shortener.validators import validate_url, validate_desired_shortcode
from url_shortener.settings import HOST

class SubmitForm(forms.Form):
    url = forms.CharField(
        label='',
        validators=[validate_url],
        widget=forms.TextInput(attrs={
            "placeholder": "Long URL",
            "class": "form-control form-control-lg"
            }
        )
    )

    short_url = forms.CharField(
        required=False,
        label='{0}'.format(HOST),
        label_suffix='/+',
        validators=[validate_desired_shortcode],
        widget=forms.TextInput(attrs={
            "placeholder": "Desire shortcode (optional)",
            "class": "form-control form-control-sm"
            }
        )
    )