from django import forms

from . import models
class SearchForm(forms.Form):
    title = forms.CharField(required=False,label='タイトル', max_length=200)
    location = forms.CharField( required=False,label='所在地', max_length=200)
class SearchFormLocate(forms.Form):
    location = forms.CharField( label='所在地', max_length=200)