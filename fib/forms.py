from django import forms


class SearchForm(forms.Form):
    number = forms.IntegerField()

    def clean_number(self):
        number = self.cleaned_data['number']
        return number
