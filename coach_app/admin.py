from django.contrib import admin
from coach_app.models import Coach

# Register your models here.


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'nama_lengkap', 'alamat_kotakab')
