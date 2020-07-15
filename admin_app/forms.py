from django import forms
from student_app.models import Student
from admin_app.models import Order


class AdminStudentDnursForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']


class AdminOrderDnursForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'student', 'coach', 'product', 'diskon',
            'tanggal_transaksi', 'tanggal_expired',
            ]
