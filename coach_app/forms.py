from django import forms
from admin_app.models import Order


class CoachOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']
