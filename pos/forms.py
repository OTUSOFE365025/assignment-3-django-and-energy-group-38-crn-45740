from django import forms

class ScanForm(forms.Form):
    upc = forms.CharField(
        max_length=32,
        label="Scan / Enter UPC",
        widget=forms.TextInput(attrs={"placeholder": "e.g. 012345678912"})
        
    )