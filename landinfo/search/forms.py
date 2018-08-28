from django import forms

#検索フォームの各フィールド
class SearchForm(forms.Form):
    room_id = forms.IntegerField(required=False, label='物件番号', widget=forms.NumberInput(attrs={'class':'form-number'}))
    title = forms.CharField(required=False, label='物件情報', max_length=200, widget=forms.TextInput(attrs={'size': 15}))
    location = forms.CharField( required=False, label='所在地', max_length=200, widget=forms.TextInput(attrs={'size': 10}))
    traffic = forms.CharField( required=False, label='最寄り駅', max_length=200, widget=forms.TextInput(attrs={'size': 10}))
    CHOICE_order = {
        ('1', '価格が安い順'),
        ('2', '価格が高い順'),
        ('3', '坪単価が安い順'),
        ('4', '坪単価が高い順'),
        ('5', '土地面積が広い順'),
        ('6', '土地面積が狭い順'),
    }

    order = forms.ChoiceField(label='順番', widget=forms.Select, choices= CHOICE_order, initial=0)
    min_price = forms.IntegerField(required=False, label='価格下限(万円)', widget=forms.NumberInput(attrs={'class':'form-number'}))
    max_price = forms.IntegerField(required=False, label='価格上限(万円)', widget=forms.NumberInput(attrs={'class':'form-number'}))
    min_area = forms.IntegerField(required=False, label='面積下限(㎡)', widget=forms.NumberInput(attrs={'class':'form-number'}))
    max_area = forms.IntegerField(required=False, label='面積上限(㎡)', widget=forms.NumberInput(attrs={'class':'form-number'}))
