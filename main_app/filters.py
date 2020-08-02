from admin_app.models import Order
import django_filters


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['student', 'coach', 'product']
