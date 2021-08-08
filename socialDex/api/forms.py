from django import forms
from django.contrib.auth.models import User

class WritePost(forms.Form):
    title = forms.CharField(label = "Title", max_length = 50 )
    content = forms.CharField(label = "Text", max_length = 524, widget= forms.Textarea )   
    isPublic = forms.BooleanField(label= "Private Post", required = False)
    