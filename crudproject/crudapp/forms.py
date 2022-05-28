from django import forms
from .models import Detail
 
class detailsform(forms.ModelForm):
    class Meta:
        model=Detail
        fields="__all__"