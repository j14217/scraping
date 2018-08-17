from django import forms

from . import models
#検索フォームの各フィールド
class SearchForm(forms.Form):
    title = forms.CharField(required=False, label='タイトル', max_length=200)
    location = forms.CharField( required=False, label='所在地', max_length=200)
    traffic = forms.CharField( required=False, label='交通', max_length=200)
    CHOICE_order = {
        ('1', '価格が安い順'),
        ('2', '価格が高い順'),
        ('3', '坪単価が安い順'),
        ('4', '坪単価が高い順'),
        ('5', '土地面積が広い順'),
        ('6', '土地面積が狭い順'),
    }

    order = forms.ChoiceField(label='順番', widget=forms.Select, choices= CHOICE_order, initial=0)
    min_price = forms.IntegerField(required=False, label='価格下限(万円)')
    max_price = forms.IntegerField(required=False, label='価格上限(万円)')
    min_area = forms.IntegerField(required=False, label='面積下限(㎡)')
    max_area = forms.IntegerField(required=False, label='面積上限(㎡)')
    
