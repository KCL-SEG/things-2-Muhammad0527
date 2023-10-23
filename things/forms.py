"""Forms of the project."""

from django import forms
from .models import Thing

class ThingsForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}

    # name = forms.CharField(label="Name")
    # description = forms.CharField(widget=forms.Textarea, label="Description")
    # quantity = forms.IntegerField(widget=forms.NumberInput, label="Quantity")
