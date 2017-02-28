from django import forms
from django.forms import extras
from datetime import datetime
from fab import models


class OEEFilterForm(forms.Form):
    year = forms.IntegerField(
        min_value=2015,
        max_value=datetime.now().year,
        required=False,
        initial=datetime.now().year,
        widget=forms.Select
    )
    month = forms.IntegerField(min_value=1, max_value=12, required=False, initial=datetime.now().month)
    day = forms.IntegerField(min_value=1, max_value=31, required=False, initial=datetime.now().day)
    presses = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=models.FabWorkcenters.objects.all(),
        required=False,
    )
    product_types = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=models.FabProductType.objects.all(),
        required=False,
    )
    compositions = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=models.FabComposition.objects.all(),
        required=False,
    )
    batch = forms.CharField()
    stockcode = forms.CharField()

