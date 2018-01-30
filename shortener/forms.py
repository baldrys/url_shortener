from django import forms

from shortener.validators import validate_url, validate_desired_shortcode


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
        label='',
        # label_suffix='/+',
        validators=[validate_desired_shortcode],
        widget=forms.TextInput(attrs={
            "placeholder": "Type the shortcode (host will be added)",
            "class": "form-control form-control-sm",
            "id": "toggle",
            "style": "display: none",
            },
        ),

    )