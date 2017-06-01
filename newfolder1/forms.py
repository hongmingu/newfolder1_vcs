from django import forms
from title.models import Title

class TitleForm(forms.ModelForm):

    class Meta:
        model = Title
        fields = ('','')