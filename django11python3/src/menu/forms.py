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
            'slug',
        ]

    # custom validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name=="hey":
            raise forms.ValidationError("Not a valid name")
        return name

    # def clean_number(self):
    #     number = self.cleaned_data.get("number")
    #     if ".edu" in number:
    #         raise forms.ValidationError("It is not a valid number")
    #     return number
