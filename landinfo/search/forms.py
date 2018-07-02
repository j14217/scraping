from django import forms

from . import models
class SearchForm(forms.Form):
    title = forms.CharField( label='タイトル', max_length=200)
