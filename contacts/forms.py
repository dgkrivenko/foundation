from django import forms

class QuestionsFrom(forms.Form):

    name = forms.CharField(
        label='name', 
        max_length=100, 
        required=True, 
        widget=forms.widgets.TextInput(attrs={'class': 'input-style', 'placeholder':'Name'}))

    email = forms.CharField(
        label='Email', 
        max_length=100, 
        required=True,
        widget=forms.widgets.TextInput(attrs={'class': 'input-style', 'placeholder':'E-mail'}))

    question = forms.CharField(
        widget=forms.widgets.Textarea(attrs={'class': 'input-style', 'placeholder':'Your question'}))