from django import forms

from .models import ContactDetails


class ContactCreateForm(forms.Form):
    name            = forms.CharField()
    relationship    = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name=="Hello":
            raise forms.ValidationError("Not a valid name")
        return name


class ContactImageCreateForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = [
            'name',
            'relationship',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name=="hey":
            raise forms.ValidationError("Not a valid name")
        return name