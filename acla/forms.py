from django import forms

from .models import Suspicious

class Alert_comment_form(forms.ModelForm):
    class Meta:
        model = Suspicious
        fields = ['status', 'comment']