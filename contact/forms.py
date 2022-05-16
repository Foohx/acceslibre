from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from erp.models import Erp
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = (
            "created_at",
            "updated_at",
            "sent_ok",
        )
        widgets = {
            "email": forms.TextInput(attrs={"autocomplete": "email"}),
            "name": forms.TextInput(attrs={"autocomplete": "family-name"}),
        }

    # hide relations
    user = forms.ModelChoiceField(
        queryset=get_user_model().objects, widget=forms.HiddenInput, required=False
    )
    erp = forms.ModelChoiceField(
        queryset=Erp.objects, widget=forms.HiddenInput, required=False
    )

    email = forms.EmailField(
        error_messages={"invalid": "Format de l'email attendu : nom@domaine.tld"}
    )

    # form specific fields
    next = forms.CharField(required=False, widget=forms.HiddenInput)
    robot = forms.BooleanField(
        label="Je ne suis pas un robot",
        help_text="Merci de cocher cette case pour envoyer votre message",
        initial=False,
        required=False,
    )

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        initial = kwargs.get("initial", {})

        # prefill initial form data
        user = request.user
        if user.is_authenticated:
            initial["name"] = (
                f"{user.first_name} {user.last_name}".strip() or f"{user.username}"
            )
            initial["email"] = user.email
            initial["user"] = user

        kwargs["initial"] = initial

        return super().__init__(*args, **kwargs)

    def clean_robot(self):
        robot = self.cleaned_data.get("robot", True)
        if not robot:
            raise ValidationError(
                mark_safe("Cochez cette case pour soumettre le formulaire.")
            )
        return robot
