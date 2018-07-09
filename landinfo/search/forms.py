from django import forms

from . import models
class SearchForm(forms.Form):
    title = forms.CharField(required=False,label='タイトル', max_length=200)
    location = forms.CharField( required=False,label='所在地', max_length=200)
    traffic = forms.CharField( required=False, label='交通', max_length=200)
