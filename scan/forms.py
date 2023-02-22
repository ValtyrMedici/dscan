from django import forms

class ScanForm(forms.Form):
    scan = forms.CharField(widget=forms.Textarea, required=True)