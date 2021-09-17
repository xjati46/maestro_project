from django.contrib import admin
from coach_app.models import Coach
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Coach)
class CoachAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'id', 'nama_lengkap', 'alamat_kotakab')
