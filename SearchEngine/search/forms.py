from django import forms


class SearchForm(forms.Form):
    user_input = forms.CharField()
