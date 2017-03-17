from django import forms

class NameForm(forms.Form):
    query = forms.CharField(label='query', max_length=100)

class Answer_form(forms.Form):
    answer_text = forms.CharField(label='answer_text', max_length=500)

