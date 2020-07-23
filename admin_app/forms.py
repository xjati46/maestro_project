from django import forms
from student_app.models import Student
from admin_app.models import Order
from tempus_dominus.widgets import DatePicker


class AdminStudentDnursForm(forms.ModelForm):
    tanggal_lahir = forms.DateField(widget=DatePicker())

    class Meta:
        model = Student
        exclude = ['user']


class AdminOrderDnursForm(forms.ModelForm):
    tanggal_transaksi = forms.DateField(widget=DatePicker())
    tanggal_expired = forms.DateField(widget=DatePicker())

    class Meta:
        model = Order
        fields = [
            'student', 'coach', 'product', 'diskon',
            'tanggal_transaksi', 'tanggal_expired',
            ]
