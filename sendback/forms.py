from .models import SendBack
from django import forms


class SendBackForm(forms.ModelForm):
    class Meta:
        model = SendBack
        fields = ('name', 'email', 'reason', 'order_number')