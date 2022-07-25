from django import forms

from entrepot.models.Zone import Zone


class AddZone(forms.Form):
    zone=forms.ModelMultipleChoiceField(queryset=Zone.objects.all(), widget = forms.SelectMultiple(attrs={'class':'form-control'}))