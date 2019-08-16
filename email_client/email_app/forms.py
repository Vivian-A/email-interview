
from django import forms

class EmailForm(forms.Form):
    sent_to = forms.CharField(label='Recipient',max_length=200)
    subject = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)